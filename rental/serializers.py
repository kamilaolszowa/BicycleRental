from typing_extensions import Self
from django.db.models import fields
from rest_framework import serializers
from .models import Customer, Reservation, Brand, Bicycle
from django.core.validators import MinValueValidator
from datetime import date


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class BicycleSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False)

    class Meta:
        model = Bicycle
        fields = ['id', 'model', 'brand', 'daily_rate', 'image_url']


class ReservationSerializer(serializers.ModelSerializer):
    bicycle = BicycleSerializer(many=False)

    class Meta:
        model = Reservation
        fields = ['id', 'date_start', 'date_end', 'bicycle', 'customer']


class UpdateReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['date_start', 'date_end', 'bicycle']


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone',  'birth_date']


class MakeReservationSerialize(serializers.Serializer):
    bicycle_id = serializers.IntegerField()
    date_start = serializers.DateField()
    date_end = serializers.DateField()

    def validate_bicycle_id(self, bicycle_id):
        if not Bicycle.objects.filter(pk=bicycle_id).exists():
            raise serializers.ValidationError(
                "No bicycle with the given ID was found.")
        return bicycle_id

    def validate_date_end(self, date_end):
        date_start = self.initial_data.get('date_start')
        if date_start > str(date_end):
            raise serializers.ValidationError(
                {"End date should be greater than start date."})
        return date_end

    def validate_date_start(self, date_start):
        if date_start < date.today():
            raise serializers.ValidationError(
                "Start date should be equal or greater than today's date.")
        return date_start

    def save(self, **kwargs):
        customer = Customer.objects.get(
            user_id=self.context['user_id'])
        bicycle_id = self.validated_data['bicycle_id']
        date_start = self.validated_data['date_start']
        date_end = self.validated_data['date_end']
        reservation = Reservation.objects.create(
            bicycle_id=bicycle_id, customer=customer, date_start=date_start, date_end=date_end)
        return reservation
