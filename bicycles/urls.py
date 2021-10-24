from django.urls import path
from . import views

app_name = 'bicycles'
# Url configuration
# Objects that map url endpoints to view functions
urlpatterns = [
    # Mapping to a view function
    path('', views.index, name='index'),
    path('<bicycle_id>', views.detail, name='detail')

]
