from django.db import models
from datetime import date
from django.db.models.deletion import CASCADE
from bicycles.models import Bicycle
from django.conf import settings
from django.contrib import admin


class Customer(models.Model):
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    # def first_name(self):
    #     return self.user.first_name

    # def last_name(self):
    #     return self.user.last_name

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']


class Reservation(models.Model):
    date_start = models.DateField(default=date.today)
    date_end = models.DateField(default=date.today)
    bicycle = models.ForeignKey(
        Bicycle, related_name='reservations', on_delete=CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    class Meta:
        permissions = [
            ('cancel_reservation', 'Can cancel reservation')
        ]
