
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from apps.forms import LoginForm


class LoginPageView(LoginView):
    form_class = LoginForm
    template_name = 'apps/login_page.html'
    next_page = reverse_lazy('main_page_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = LoginForm
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)