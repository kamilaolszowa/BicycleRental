from django.db.models import fields
from rest_framework import serializers
from .models import Customer, Reservation, Brand, Bicycle


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'date_start', 'date_end', 'bicycle']


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone',  'birth_date']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class BicycleSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False)

    class Meta:
        model = Bicycle
        fields = ['id', 'model', 'brand', 'daily_rate']
