from django.urls import path

from apps.views import LoginPageView
from apps.views import ProfileSettingView, ProductListView

urlpatterns = [
    path('edit-profile', ProfileSettingView.as_view(), name='edit_profile_view'),
    path('products', ProductListView.as_view(), name='products'),
    path('edit-profile/', ProfileSettingView.as_view(), name='edit_profile_view'),
    path('products/', ProductListView.as_view(), name='products'),
    path('login/', LoginPageView.as_view(), name='login_view'),

]
