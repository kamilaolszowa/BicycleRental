from django.urls import path
from . import views

app_name = 'reservations'
# Url configuration
# Objects that map url endpoints to view functions
urlpatterns = [
    # Mapping to a view function
    path('', views.reservation_list),
    path('<int:reservation_id>', views.reservation_detail)

]
