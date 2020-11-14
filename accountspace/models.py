from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_bewerber = models.BooleanField(default=False)
    is_ausschuss = models.BooleanField(default=False)
