from django.db.models import fields
from rest_framework import serializers

from bicycles.models import Bicycle, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class BicycleSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Bicycle
        fields = ['id', 'model', 'brand', 'daily_rate']
