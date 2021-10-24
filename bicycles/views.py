from django.contrib.admin import options
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from . models import Bicycle

# Main page of app


def index(request):
    bicycles = Bicycle.objects.all()
    # Bicycle.objects.filter(release_year=2018)
    # Movie.object.get(id=1)
    # output = ', '.join([b.model for b in bicycles])
    # return HttpResponse(output)
    return render(request, 'bicycles/index.html', {'bicycles': bicycles})


def detail(request, bicycle_id):
    bicycle = get_object_or_404(Bicycle, pk=bicycle_id)
    return render(request, 'bicycles/detail.html', {'bicycle': bicycle})
    # TODO
    # ValueError
