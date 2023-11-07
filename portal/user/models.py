from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *
from country.models import country
# Create your models here.

class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=12)
    country = models.ForeignKey(country, on_delete= models.CASCADE,null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        EMPLOYEE = "EMPLOYEE", 'Employee'
        GUEST = "GUEST", "Guest"

    role = models.CharField(max_length=50, choices=Role.choices)