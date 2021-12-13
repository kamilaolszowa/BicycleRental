from django.urls import path
from . import views
from django.urls import path
from django.contrib import admin

# app_name = 'bicycles'
# # Url configuration
# # Objects that map url endpoints to view functions
# urlpatterns = [
#     # Mapping to a view function
#     path('', views.index, name='index'),
#     path('<int:bicycle_id>', views.bicycle_detail)

# ]


from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.BicycleViewSet)

urlpatterns = router.urls
