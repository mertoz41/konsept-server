from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=75)
    address = models.CharField(max_length=100)
    property_type = models.CharField(max_length=15)
    price = models.PositiveIntegerField()
    for_sale = models.BooleanField()
    room_number = models.PositiveIntegerField()
    year_built = models.PositiveIntegerField()
    square_meter = models.PositiveIntegerField()

    def __str__(self):
        return self.title

# Create your models here.
