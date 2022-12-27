from django.forms import ModelForm, CharField, EmailField


class RegisterForm(ModelForm):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=255)
    phone = CharField(max_length=25)
    email = EmailField(max_length=255)


