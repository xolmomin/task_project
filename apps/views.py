from django.views.generic import TemplateView

from apps.forms import RegisterForm


class RegisterPage(TemplateView):
    form_class = RegisterForm
    template_name = 'apps/register.html'
