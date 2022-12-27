from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import UpdateView, ListView

from apps.forms import LoginForm
from apps.forms import RegisterForm
from apps.models import User, Product


class RegisterPage(TemplateView):
    model = RegisterForm
    template_name = 'apps/register.html'
    success_url = reverse_lazy('register_view')


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
    paginate_by = 5
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = Product.objects.all()
        return context


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


class IndexListView(ListView):
    queryset = Product.objects.first()
    template_name = 'apps/index.html'
    context_object_name = 'profile'
