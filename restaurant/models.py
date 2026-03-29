from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title} : {self.price:.2f}'


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

    class Meta:
        ordering = ['booking_date', 'name']

    def __str__(self):
        return f'{self.name} - {self.booking_date} ({self.no_of_guests} guests)'
