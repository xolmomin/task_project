from django.contrib.auth.models import AbstractUser

from django.db.models import Model, CharField, TextField, ImageField, EmailField, SlugField
from django.utils.text import slugify


class Product(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = CharField(max_length=255)
    image = ImageField(upload_to='product/')
    slug = SlugField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            while Product.objects.filter(slug=self.slug).exists():
                slug = Product.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

            super().save(*args, **kwargs)


class User(AbstractUser):
    email = EmailField(max_length=255, unique=True)
    phone = CharField(max_length=255, unique=True)
    image = ImageField(upload_to='%m', null=True, blank=True)
    biography = TextField(null=True, blank=True)
    REQUIRED_FIELDS = ['email', 'password', 'phone']
