from django.db import models
from django.db.models.fields import related
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Bicycle(models.Model):
    model = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
