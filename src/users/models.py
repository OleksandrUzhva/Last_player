from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .enums import Positions

class User(models.Model):
    login = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30, unique=True)

    is_staff = models.BooleanField(
        default=False,
    )
    is_superuser = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(default=timezone.now)
    
    positions = models.CharField(
        max_length=20, default=Positions.SUPPORT, choices=Positions.choices()
    )

