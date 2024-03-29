"""BicycleRental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.models import BicycleResource, ReservationResource
from . import views

bicycle_resource = BicycleResource()
reservations_resource = ReservationResource()

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('rental/', include('rental.urls')),
    path('api/bicycle/', include(bicycle_resource.urls)),
    path('api/reservations/', include(reservations_resource.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include('debug_toolbar.urls'))
]
