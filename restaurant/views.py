from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


# --- Static page views ---

def index(request):
    return render(request, 'index.html')

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def book(request):
    return render(request, 'booking.html')


# --- Menu API views ---

class MenuItemView(generics.ListCreateAPIView):
    """
    GET  /restaurant/menu/items/  - List all menu items.
    POST /restaurant/menu/items/  - Create a new menu item.
    No authentication required.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /restaurant/menu/items/<id>/ - Retrieve a single item.
    PUT    /restaurant/menu/items/<id>/ - Replace an item.
    PATCH  /restaurant/menu/items/<id>/ - Partially update an item.
    DELETE /restaurant/menu/items/<id>/ - Remove an item.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_object(self):
        return get_object_or_404(Menu, pk=self.kwargs['pk'])


# --- Booking API viewset (authentication required) ---

class BookingViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for table bookings.
    All actions require a valid authentication token.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
