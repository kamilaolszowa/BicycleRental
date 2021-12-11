from django.db.models import fields
from rest_framework import serializers

from bicycles.models import Bicycle, Brand


class BicycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicycle
        fields = ['id', 'model', 'brand', 'daily_rate']
