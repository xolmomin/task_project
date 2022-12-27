from django.views.generic import TemplateView

from apps.forms import RegisterForm


class RegisterPage(TemplateView):
    model = RegisterForm
    template_name =