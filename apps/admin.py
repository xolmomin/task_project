from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import User, Product


@admin.register(User)
class User(ModelAdmin):
    list_display = ('username', 'first_name', 'email')
    exclude = ('last_login', 'groups', 'user_permissions', 'date_joined')


@admin.register(Product)
class ProductsAdmin(ModelAdmin):
    pass
