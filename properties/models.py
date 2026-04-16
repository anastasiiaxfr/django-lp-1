from datetime import datetime

from django.db import models

from realtors.models import Realtor

# Create your models here.
class Property(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    price = models.IntegerField()
    area = models.IntegerField()
    floor = models.IntegerField()
    parking = models.IntegerField()
    property_type = models.CharField(max_length=50)
    rent_date = models.DateTimeField(default=datetime.now, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    is_published = models.BooleanField(default=True)
   

    def __str__(self):
        return self.title
