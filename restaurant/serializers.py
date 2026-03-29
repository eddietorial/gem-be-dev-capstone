from rest_framework import serializers
from .models import Menu, Booking


class MenuSerializer(serializers.ModelSerializer):
    """Converts Menu model instances to and from JSON."""

    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than zero.')
        return value

    def validate_inventory(self, value):
        if value < 0:
            raise serializers.ValidationError('Inventory cannot be negative.')
        return value


class BookingSerializer(serializers.ModelSerializer):
    """Converts Booking model instances to and from JSON."""

    class Meta:
        model = Booking
        fields = '__all__'

    def validate_no_of_guests(self, value):
        if value < 1:
            raise serializers.ValidationError(
                'A booking must include at least one guest.'
            )
        return value
