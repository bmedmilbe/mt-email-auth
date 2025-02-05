from django.conf import settings
from django.db import models
from uuid import uuid4
from pprint import pprint
from django.core.validators import MinValueValidator
from datetime import datetime


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    visible = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

class Org(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='orgs')
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True,blank=True)
    address = models.CharField(max_length=255, null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Post(models.Model):
    org = models.ForeignKey(
        Org, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.title}"
    

    
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self) -> str:
        return f"{self.comment}"

class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='likes')
    
    def __str__(self) -> str:
        return f"{self.customer}"
    
class Area(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
    
class CustomerArea(models.Model):
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name='customers')
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='areas')
    

    def __str__(self) -> str:
        return f"{self.area}"
    
    class Meta():
        unique_together = ['customer', 'area']

class OrgArea(models.Model):
    
    org = models.ForeignKey(
        Org, on_delete=models.CASCADE, related_name='areas')
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name='orgs')

    def __str__(self) -> str:
        return f"{self.area}"
    class Meta():
        unique_together = ['org', 'area']
    
class PostArea(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='areas')
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name='posts')
    
    def __str__(self) -> str:
        return f"{self.area}"
    
    class Meta():
        unique_together = ['post', 'area']
