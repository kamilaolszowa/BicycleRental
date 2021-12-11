from django.db import models
from datetime import date
from django.db.models.deletion import CASCADE
from bicycles.models import Bicycle


class Reservation(models.Model):
    date_start = models.DateField(default=date.today)
    date_end = models.DateField(default=date.today)
    bicycle = models.ForeignKey(
        Bicycle, related_name='reservations', on_delete=CASCADE)
