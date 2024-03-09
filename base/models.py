from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    


# Create your models here.
