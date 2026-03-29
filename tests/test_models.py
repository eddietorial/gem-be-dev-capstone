from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuModelTest(TestCase):

    def setUp(self):
        self.item = Menu.objects.create(
            title='Grilled Sea Bass',
            price=18.50,
            inventory=12,
        )

    def test_menu_item_created(self):
        fetched = Menu.objects.get(pk=self.item.pk)
        self.assertEqual(fetched.title, 'Grilled Sea Bass')
        self.assertEqual(float(fetched.price), 18.50)
        self.assertEqual(fetched.inventory, 12)

    def test_menu_str_representation(self):
        self.assertEqual(str(self.item), 'Grilled Sea Bass : 18.50')

    def test_menu_ordering(self):
        Menu.objects.create(title='Baklava', price=4.50, inventory=20)
        Menu.objects.create(title='Hummus', price=7.00, inventory=30)
        titles = list(Menu.objects.values_list('title', flat=True))
        self.assertEqual(titles, sorted(titles))


class BookingModelTest(TestCase):

    def setUp(self):
        self.booking = Booking.objects.create(
            name='Geoffrey Moraes',
            no_of_guests=4,
            booking_date='2026-04-01',
        )

    def test_booking_created(self):
        fetched = Booking.objects.get(pk=self.booking.pk)
        self.assertEqual(fetched.name, 'Geoffrey Moraes')
        self.assertEqual(fetched.no_of_guests, 4)
        self.assertEqual(str(fetched.booking_date), '2026-04-01')

    def test_booking_str_representation(self):
        expected = 'Geoffrey Moraes - 2026-04-01 (4 guests)'
        self.assertEqual(str(self.booking), expected)
