from django.contrib.admin import options
from django.db.models import query
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
# from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bicycle
from .serializers import BicycleSerializer
# from rest_framework.viewsets import ModelViewSet

# Main page of app

# TO DO
# turn into class BicycleViewSet(ReadOnlyModelViewSet):


@api_view()
def index(request):
    queryset = Bicycle.objects.all()
    serializer = BicycleSerializer(queryset, many=True)
    return Response(serializer.data)

# def index(request):
#     bicycles = Bicycle.objects.all()
#     # Bicycle.objects.filter(release_year=2018)
#     # Movie.object.get(id=1)
#     # output = ', '.join([b.model for b in bicycles])
#     # return HttpResponse(output)
#     return render(request, 'bicycles/index.html', {'bicycles': bicycles})


@api_view()
def bicycle_detail(request, bicycle_id):
    bicycle = get_object_or_404(Bicycle, pk=bicycle_id)
    serializer = BicycleSerializer(bicycle)
    return Response(serializer.data)


# def detail(request, bicycle_id):
#     bicycle = get_object_or_404(Bicycle, pk=bicycle_id)
#     return render(request, 'bicycles/detail.html', {'bicycle': bicycle})
#     # TODO
#     # ValueError
