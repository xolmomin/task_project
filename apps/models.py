from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models import Model, CharField, TextField, ImageField, EmailField


class Product(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = CharField(max_length=255)
    image = ImageField(upload_to='product/')


class User(AbstractUser):
    email = EmailField(max_length=255, unique=True)
    phone = CharField(max_length=255, unique=True)
    image = ImageField(upload_to='%m', null=True, blank=True)
    biography = TextField(null=True, blank=True)
    REQUIRED_FIELDS = ['email', 'password', 'phone']
