from django.http.response import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from bicycles import serializers
from rest_framework import status
import reservations
from .models import Reservation
from .serializers import ReservationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# generic views


class ReservationList(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    # def get(self, request):
    #     queryset = Reservation.objects.all()
    #     serializer = ReservationSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = ReservationSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReservationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    # def patch(self, request, reservation_id):
    #     reservation = get_object_or_404(Reservation, pk=reservation_id)
    #     serializer = ReservationSerializer(reservation, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    def delete(self, request, reservation_id):
        reservation = get_object_or_404(Reservation, pk=reservation_id)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
