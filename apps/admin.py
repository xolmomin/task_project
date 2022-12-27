from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from apps.models import Product


@admin.register(Product)
class ProductsAdmin(ModelAdmin):
    pass