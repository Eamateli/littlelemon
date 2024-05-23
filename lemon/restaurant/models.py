from django.db import models

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'
        
    def __str__(self):
        return f"{self.title} : {str(self.price)}"


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    number_of_guests = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'
        
    def __str__(self):
        return f"{self.name} for {self.number_of_guests} guests on {self.booking_date}"