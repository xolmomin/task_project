from django.urls import path

from apps.views import LoginPageView, RegisterPage, ProfileSettingView, ProductListView, indexListView

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register_view'),
    path('edit-profile/', ProfileSettingView.as_view(), name='edit_profile_view'),
    path('products/', ProductListView.as_view(), name='products'),
    path('login/', LoginPageView.as_view(), name='login_view'),
    path('', indexListView.as_view(), name='index'),
]
