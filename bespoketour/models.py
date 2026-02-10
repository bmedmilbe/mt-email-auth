from django.db import models
from django.conf import settings

# Create your models here.

class ProfileType(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image=models.CharField(max_length=255, unique=True)

class BespokeTag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    image=models.CharField(max_length=255, unique=True)


class ProfileTag(models.Model):
    profile_type = models.ForeignKey(ProfileType, on_delete=models.CASCADE)
    bespoke_tag = models.ForeignKey(BespokeTag, on_delete=models.CASCADE)


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="troca_customer")
    def __str__(self):
        return self.user.first_name

    profile_type = models.ForeignKey(ProfileType, on_delete=models.SET_NULL, null=True)

class CustomerTag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bespoke_tag = models.ForeignKey(BespokeTag, on_delete=models.CASCADE)


