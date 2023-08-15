from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255, null=True)
    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["username"]  # removes email from REQUIRED_FIELDS
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS
