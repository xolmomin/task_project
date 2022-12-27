from django.forms import ModelForm, CharField, EmailField

from apps.models import User


class RegisterForm(ModelForm):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=255)
    phone = CharField(max_length=25)
    email = EmailField(max_length=255)


class EditProfile(ModelForm):
    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'email', 'phone', 'biography')
