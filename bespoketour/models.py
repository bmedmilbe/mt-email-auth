from django.db import models
from django.conf import settings

# Create your models here.

class ProfileType(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image=models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.title
class BespokeTag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    image=models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.title

class ProfileTag(models.Model):
    profile_type = models.ForeignKey(ProfileType, on_delete=models.CASCADE, related_name='profile_tags')
    bespoke_tag = models.ForeignKey(BespokeTag, on_delete=models.CASCADE, related_name='profile_tags')
    
    class Meta():
        unique_together = ["profile_type", "bespoke_tag"]

class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bespoketour_customer")
    def __str__(self):
        return self.user.first_name

    profile_type = models.ForeignKey(ProfileType, on_delete=models.SET_NULL, null=True, related_name='customer_profile')

class CustomerTag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bespoke_tag = models.ForeignKey(BespokeTag, on_delete=models.CASCADE)


