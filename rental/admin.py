from django.contrib import admin
from .serializers import ReservationSerializer
from .models import Reservation, Customer, Brand, Bicycle


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'bicycle', 'date_start', 'date_end')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__isstartswith', 'last_name__isstartswith']


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BicycleAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('model', 'daily_rate')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Bicycle, BicycleAdmin)


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Customer, CustomerAdmin)
