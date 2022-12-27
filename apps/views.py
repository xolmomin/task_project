from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.models import User
from django.views.generic import TemplateView

from apps.forms import RegisterForm


class RegisterPage(TemplateView):
    model = RegisterForm
    template_name = 'register.html'


class ProfileSettingView(UpdateView):
    form_class = UpdateView
    model = User
    template_name = 'edit-profile.html'
    success_url = reverse_lazy('edit_profile_view')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
