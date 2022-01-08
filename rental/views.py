from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.viewsets import ModelViewSet
from django.urls import path
from django.contrib import admin
from django.core.exceptions import ValidationError

# generic views


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
