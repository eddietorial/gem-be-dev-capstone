from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title='Greek Salad',   price=12.99, inventory=10)
        self.item2 = Menu.objects.create(title='Bruschetta',    price=5.99,  inventory=15)
        self.item3 = Menu.objects.create(title='Lemon Dessert', price=6.99,  inventory=8)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(response.data), 3)

    def test_create_menu_item(self):
        data = {'title': 'New Item', 'price': 15.99, 'inventory': 5}
        response = self.client.post(reverse('menu-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 4)

    def test_get_single_menu_item(self):
        response = self.client.get(reverse('menu-detail', args=[self.item1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.item1.title)

    def test_get_nonexistent_item_returns_404(self):
        response = self.client.get(reverse('menu-detail', args=[9999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_menu_item(self):
        data = {'price': 14.99}
        response = self.client.patch(
            reverse('menu-detail', args=[self.item1.id]),
            data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item1.refresh_from_db()
        self.assertEqual(float(self.item1.price), 14.99)

    def test_delete_menu_item(self):
        response = self.client.delete(reverse('menu-detail', args=[self.item1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 2)


class BookingViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='gem_tester', password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.booking = Booking.objects.create(
            name='Geoffrey Moraes', no_of_guests=4, booking_date='2026-04-01'
        )

    def test_unauthenticated_request_rejected(self):
        unauthenticated = APIClient()
        response = unauthenticated.get('/restaurant/booking/tables/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_list_bookings(self):
        response = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_booking(self):
        data = {
            'name': 'Jane Smith',
            'no_of_guests': 2,
            'booking_date': '2026-04-02',
        }
        response = self.client.post(
            '/restaurant/booking/tables/', data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)

    def test_create_booking_zero_guests_rejected(self):
        data = {'name': 'Zero Guest', 'no_of_guests': 0, 'booking_date': '2026-04-02'}
        response = self.client.post(
            '/restaurant/booking/tables/', data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_single_booking(self):
        response = self.client.get(f'/restaurant/booking/tables/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Geoffrey Moraes')

    def test_update_booking_guest_count(self):
        response = self.client.patch(
            f'/restaurant/booking/tables/{self.booking.id}/',
            {'no_of_guests': 6},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.no_of_guests, 6)

    def test_delete_booking(self):
        response = self.client.delete(
            f'/restaurant/booking/tables/{self.booking.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)
