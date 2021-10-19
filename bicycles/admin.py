from django.contrib import admin
from . models import Brand, Bicycle


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BicycleAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('model', 'number_in_stock', 'daily_rate')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Bicycle, BicycleAdmin)
