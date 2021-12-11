from django.urls import path
from . import views

app_name = 'reservations'
# Url configuration
# Objects that map url endpoints to view functions
urlpatterns = [
    # Mapping to a view function
    path('', views.ReservationList.as_view()),
    path('<int:pk>', views.ReservationDetail.as_view())

]
