from django.contrib.admin import options
from django.http import HttpResponse
from django.shortcuts import render
from . models import Bicycle

# Main page of app


def index(request):
    bicycles = Bicycle.objects.all()
    # Bicycle.objects.filter(release_year=2018)
    # Movie.object.get(id=1)
    # output = ', '.join([b.model for b in bicycles])
    # return HttpResponse(output)
    return render(request, 'bicycles/index.html', {'bicycles': bicycles})
