from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import Model, CharField, TextField, ImageField, EmailField


class Product(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = CharField(max_length=255)
    image = ImageField(upload_to='product/')


class User(AbstractUser):
    email = EmailField(max_length=255, unique=True)
    phone = CharField(max_length=255, unique=True)
    image = ImageField(upload_to='%m', null=True, blank=True, max_length=300)
    biography = TextField(null=True, blank=True)
