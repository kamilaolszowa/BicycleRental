from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register('', views.ReservationViewSet)

urlpatterns = router.urls
