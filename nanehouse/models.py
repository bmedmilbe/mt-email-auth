from django.db import models

# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from uuid import uuid4

from django.conf import settings

class Customer(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="nane_customers")
    
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
    

class Currency(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)

    def __str__(self) -> str:
        return f"{self.code.upper()}"

class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255)
    def __str__(self) -> str:
        return self.name

    
class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="ccitiess") 
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    def __str__(self) -> str:
        return self.name
class Street(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="streets") 
    slug = models.SlugField(max_length=255)
    def __str__(self) -> str:
        return self.name
    
class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="clients") 
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.email}"
    

class House(models.Model):
    number = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="houses")
    active = models.BooleanField(default=False)
    price_for_nane = models.DecimalField(max_digits=8, decimal_places=2)
    price_rent = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    price_sell = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    rooms = models.IntegerField(null=True, blank=True)
    bath_room = models.IntegerField()
    description = models.TextField()
    energy_level =  models.CharField(max_length=1)
    avaliable_from = models.DateField(null=True, blank=True)

    active = models.BooleanField(default=True)
    TYPE_STUDIO = "ST"
    TYPE_FLAT = "FL"
    TYPE_APARTMENT = "AP"
    TYPE_HOUSE_SHARE = "HS"
    TYPE_HOUSE_ALL = "HA"

   

    TYPE_CHOICES = [
        (TYPE_FLAT, "Flat"),
        (TYPE_STUDIO, "Studio"),
        (TYPE_APARTMENT, "Apartment"),
        (TYPE_APARTMENT, "House Share"),
        (TYPE_APARTMENT, "House"),
    ]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)


    def __str__(self) -> str:
        return f"{self.number} {self.street} {self.street.city}"

class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="images")
    image = models.FileField(upload_to='nanehouse/house')
    def __str__(self) -> str:
        return self.image.url
    

class ClientHouse(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    house = models.ForeignKey(House, on_delete=models.PROTECT, related_name="clients_house")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) # when buy


    def __str__(self) -> str:
        return f"{self.client} {self.house}"
    
class ClientPayment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="client_payments")
    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True, null=True)
    def __str__(self) -> str:
        return f"{self.client} {self.value}"
    
class OwnerPayment(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="owner_payments")
    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True, null=True)
    def __str__(self) -> str:
        return f"{self.client} {self.value}"
    


