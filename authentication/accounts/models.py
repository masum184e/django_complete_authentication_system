from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']
