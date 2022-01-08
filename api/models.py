from django.db import models
from tastypie.resources import ModelResource
from rental.models import Bicycle
from rental.models import Reservation

# we use this to represent a concept of a bicycle in restful api


class BicycleResource(ModelResource):
    # defines metadata about bicycle resources
    class Meta:
        # returns query (lazy object); it is not going to go to db and get list of all bicycles
        queryset = Bicycle.objects.all()
        # endpoint
        resource_name = 'bicycles'
        excludes = ['date_created']


class ReservationResource(ModelResource):
    # defines metadata about reservations resources
    class Meta:
        # returns query (lazy object); it is not going to go to db and get list of all reservation
        queryset = Reservation.objects.all()
        # endpoint
        resource_name = 'reservations'
