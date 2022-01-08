from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('reservations', views.ReservationViewSet)
router.register('bicycles', views.BicycleViewSet, basename='bicycles')
router.register('customers', views.CustomerViewSet)


# URLConf
urlpatterns = router.urls
