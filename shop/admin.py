from django.contrib import admin

# Register your models here.
from shop import models


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    pass