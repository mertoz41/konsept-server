from django.db import models
from s3direct.fields import S3DirectField
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
    
class Image(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image = S3DirectField(dest='images', blank=True)