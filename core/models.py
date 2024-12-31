from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    valid = models.BooleanField(default=False)
    backstaff = models.BooleanField(default=False)
    parthner = models.IntegerField(default=1, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # removes email from REQUIRED_FIELDS
    
    # REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


