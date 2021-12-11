from django.shortcuts import render
from rest_framework.decorators import api_view

import reservations
from .models import Reservation
from .serializers import ReservationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


@api_view()
def reservation_list(request):
    queryset = Reservation.objects.all()
    serializer = ReservationSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def reservation_detail(request, reservation_id):
    bicycle = get_object_or_404(Reservation, pk=reservation_id)
    serializer = ReservationSerializer(bicycle)
    return Response(serializer.data)
