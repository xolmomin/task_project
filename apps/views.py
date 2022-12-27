from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView
from django.views.generic import TemplateView

from apps.models import User, Product
from django.views.generic import TemplateView
from apps.forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView

from apps.forms import RegisterForm


class RegisterPage(TemplateView):
    model = RegisterForm
    template_name = 'apps/register.html'


class ProfileSettingView(UpdateView):
    form_class = UpdateView
    model = User
    template_name = 'apps/edit-profile.html'
    success_url = reverse_lazy('edit_profile_view')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product_list.html'
    context_object_name = 'products'



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
