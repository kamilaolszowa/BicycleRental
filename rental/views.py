from django.db.models import query
from django.http import response
from django.urls import path
from django.contrib import admin
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
from rental.permissions import IsAdminOrReadOnly
from .models import Customer, Reservation, Bicycle
from .serializers import CustomerSerializer, ReservationSerializer, BicycleSerializer


# generic views


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    # method called action; this one is custom
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class BicycleViewSet(ModelViewSet):
    serializer_class = BicycleSerializer
    queryset = Bicycle.objects.select_related('brand').all()
    permission_classes = [IsAdminOrReadOnly]
