from .models import Bicycle
from rental.models import Reservation
from rest_framework.viewsets import ReadOnlyModelViewSet
# from rest_framework.filters import OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BicycleSerializer
from datetime import datetime


# Main page of app

# TO DO
# turn into class BicycleViewSet(ReadOnlyModelViewSet):


class BicycleViewSet(ReadOnlyModelViewSet):
    serializer_class = BicycleSerializer
    queryset = Bicycle.objects.select_related('brand').all()
    # filer_backernds = [DjangoFilterBackend]
    # ordering_fields = ['brand', 'release_year', 'daily_rate']

    # def get_queryset(self):
    #     # queryset = Bicycle.objects.all()
    #     # queryset =  super().get_queryset()

    #     # getting param value from url
    #     date_start_string = str(
    #         self.request.query_params.get('date_start')).lower()
    #     date_end_string = str(
    #         self.request.query_params.get('date_end')).lower()

    #     # converting date string to date object
    #     date_start_object = datetime.strptime(date_start_string, '%Y-%m-%d')
    #     date_end_object = datetime.strptime(date_end_string, '%Y-%m-%d')

    #     reservations = Reservation.objects.all()
    #     for reservation in reservations:


# @api_view()
# def index(request):
#     queryset = Bicycle.objects.all()
#     serializer = BicycleSerializer(queryset, many=True)
#     return Response(serializer.data)


# def index(request):
#     bicycles = Bicycle.objects.all()
#     # Bicycle.objects.filter(release_year=2018)
#     # Movie.object.get(id=1)
#     # output = ', '.join([b.model for b in bicycles])
#     # return HttpResponse(output)
#     return render(request, 'bicycles/index.html', {'bicycles': bicycles})


# @api_view()
# def bicycle_detail(request, bicycle_id):
#     bicycle = get_object_or_404(Bicycle, pk=bicycle_id)
#     serializer = BicycleSerializer(bicycle)
#     return Response(serializer.data)


# def detail(request, bicycle_id):
#     bicycle = get_object_or_404(Bicycle, pk=bicycle_id)
#     return render(request, 'bicycles/detail.html', {'bicycle': bicycle})
