from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *
# Create your models here.

class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=12)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        EMPLOYEE = "EMPLOYEE", 'Employee'
        GUEST = "GUEST", "Guest"

    role = models.CharField(max_length=50, choices=Role.choices)