from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, EmailField

from apps.models import User


class RegisterForm(ModelForm):
    full_name = CharField(max_length=50)
    phone = CharField(max_length=25)
    email = EmailField(max_length=255)


class LoginForm(ModelForm):
    def clean_password(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.get(username=username)
        if user and not user.check_password(password):
            raise ValidationError('Please check Username or password !')
        return password
