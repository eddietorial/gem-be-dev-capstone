from django.contrib import admin
from .models import Menu, Booking


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory')
    search_fields = ('title',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'booking_date', 'no_of_guests')
    list_filter = ('booking_date',)
    search_fields = ('name',)
