from django.forms import ModelForm, CharField, EmailField


class RegisterForm(ModelForm):
    full_name = CharField(max_length=50)
    phone = CharField(max_length=25)
    email = EmailField(max_length=255)



