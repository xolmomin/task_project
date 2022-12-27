from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView

from apps.models import User, Product
from django.views.generic import TemplateView

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
    paginate_by = 5
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = Product.objects.all()
        return context
