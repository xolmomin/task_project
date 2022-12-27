from django.db import models

# Create your models here.
from django.db.models import Model, CharField, TextField, ImageField


class Product(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = CharField(max_length=255)
    image = ImageField(upload_to='product/')
