from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_bewerber = models.BooleanField(default=False)
    is_ausschuss = models.BooleanField(default=False)


class Bewerber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    street = models.CharField(max_length=30, default='')
    post_code = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=12, default='')

    def __str__(self):
        return '{}'.format(self.email)
