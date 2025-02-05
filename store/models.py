from django.conf import settings
from django.db import models
from uuid import uuid4
from pprint import pprint
from django.core.validators import MinValueValidator
from datetime import datetime


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="store_customers")

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
    

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"
    

    
class Product(models.Model):
    #capa ... para samsung A25 A23 etc
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    price = models.PositiveIntegerField()
    price_off = models.PositiveIntegerField()

    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"


class Identity(models.Model):
    #Samsung GALAXY A25
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Match(models.Model):

    # Samsung GALAXY A25 | capa ... para samsung A25 A23 etc

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='matches')

    identity = models.ForeignKey(Identity, on_delete=models.CASCADE, related_name='matches')

    def __str__(self) -> str:
        return f"{self.identity.name} | {self.product.name}"
    
    class Meta():
         unique_together = ['identity', 'product']

class Color(models.Model):
    name = models.CharField(max_length=255, unique=True)
    hexcolor = models.CharField(max_length=7, unique=True)


    def __str__(self) -> str:
        return f"{self.name}"
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='store/product')
    #add color when adding picture
    class Meta():
         unique_together = ['product', 'color']

    def __str__(self) -> str:
        return f"{self.color.name} | {self.product.name}"

class OrderCustomer(models.Model):

    phone = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.phone}"

class Order(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4)
    reference = models.CharField(max_length=255,unique=True)
    # 2545 - 0321251
    # 25#year
    # 45#2 last number phone
    # 032#witch day of year
    # 21:51 #time and minut of order
    created_at = models.DateTimeField(auto_now_add=True)
    
    customer = models.ForeignKey(OrderCustomer, on_delete=models.PROTECT)

    image = models.ForeignKey(ProductImage, on_delete=models.PROTECT, related_name='orders')
    
    quantity = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"{self.reference} | {self.image.product.name}"
    
    
class OrderStatus(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    status = models.TextField()

    def __str__(self) -> str:
        return f"{self.order.reference} | {self.status}"
    