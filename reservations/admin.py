from django.contrib import admin
from .serializers import ReservationSerializer
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('date_start', 'date_end', 'bicycle')


admin.site.register(Reservation, ReservationAdmin)
