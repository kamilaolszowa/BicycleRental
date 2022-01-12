from typing_extensions import Self
from django.db.models import fields
from rest_framework import serializers
from .models import Customer, Reservation, Brand, Bicycle
from django.core.validators import MinValueValidator


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


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'phone',  'birth_date']


class MakeReservationSerialize(serializers.Serializer):
    # bicycle_id = serializers.IntegerField(validators=[MinValueValidator(1)])
    bicycle_id = serializers.IntegerField()

    def save(self, **kwargs):
        print(self.validated_data['bicycle_id'])
        print(self.context['user_id'])
        (customer, created) = Customer.objects.get_or_create(
            user_id=self.context['user_id'])
        bicycle_id = self.validated_data['bicycle_id']
        Reservation.objects.create(
            bicycle_id=bicycle_id, customer=customer)
