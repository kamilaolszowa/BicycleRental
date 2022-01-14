from decimal import Context
import re
from django import http
from django.db.models import query
from django.http import response
from django.urls import path
from django.contrib import admin
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.mixins import ListModelMixin
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
from rental.permissions import IsAdminOrReadOnly
from .models import Customer, Reservation, Bicycle
from .serializers import AllReservationSerializer, CustomerSerializer, MakeReservationSerialize, ReservationSerializer, BicycleSerializer, UpdateReservationSerializer


# generic views
# class AllReservationViewSet(ReadOnlyModelViewSet):
class AllReservationViewSet(ListModelMixin, GenericViewSet):
    queryset = Reservation.objects.all()
    serializer_class = AllReservationSerializer


class ReservationViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = MakeReservationSerialize(data=request.data, context={
                                              'user_id': self.request.user.id})
        serializer.is_valid(raise_exception=True)
        reservation = serializer.save()
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MakeReservationSerialize
        elif self.request.method == 'PATCH':
            return UpdateReservationSerializer
        return ReservationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Reservation.objects.all()

        customer_id = Customer.objects.only(
            'id').get(user_id=user.id)
        return Reservation.objects.filter(customer_id=customer_id)


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    # method called action; this one is custom
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Customer.objects.get(
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
