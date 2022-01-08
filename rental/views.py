from django.db.models import query
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.serializers import ModelSerializer
from .models import Customer, Reservation, Bicycle
from .serializers import CustomerSerializer, ReservationSerializer, BicycleSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
from django.urls import path
from django.contrib import admin
from django.core.exceptions import ValidationError

# generic views


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class BicycleViewSet(ReadOnlyModelViewSet):
    serializer_class = BicycleSerializer
    queryset = Bicycle.objects.select_related('brand').all()
