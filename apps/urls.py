from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('edit-profile/', ProfileSettingView.as_view(), name='edit_profile_view'),
]