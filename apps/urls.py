from django.contrib import admin
from django.urls import path

from apps.views import ProfileSettingView, ProductListView

urlpatterns = [
    path('edit-profile/', ProfileSettingView.as_view(), name='edit_profile_view'),
    path('products/', ProductListView.as_view(), name='products')
]
