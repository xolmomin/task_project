from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, EmailField

from apps.models import User


class RegisterForm(ModelForm):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=255)
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


class EditProfile(ModelForm):
    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'email', 'phone', 'biography')
