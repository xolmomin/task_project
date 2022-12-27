from django.contrib import admin
from django.urls import path, include

from apps.views import ProfileSettingView, ProductListView

urlpatterns = [
    path('edit-profile', ProfileSettingView.as_view(), name='edit_profile_view'),
    path('', include('apps.urls')),
    path('products', ProductListView.as_view(), name='products')
]
