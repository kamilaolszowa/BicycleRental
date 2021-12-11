from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.utils import timezone
from datetime import date


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# part of a data model; we use that to get data from db


class Bicycle(models.Model):
    model = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return str(self.brand) + " " + self.model
