from django.urls import path
from . import views

# Url configuration
# Objects that map url endpoints to view functions
urlpatterns = [
    # Mapping to a view function
    path('', views.index, name='index')

]
