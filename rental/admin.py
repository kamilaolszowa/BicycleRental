from django.contrib import admin
from .serializers import ReservationSerializer
from .models import Reservation, Customer


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'bicycle', 'date_start', 'date_end')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__isstartswith', 'last_name__isstartswith']


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Customer, CustomerAdmin)
