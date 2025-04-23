from django.conf import settings
from django.db import models

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ground_customer")
    def __str__(self):
        return self.user.first_name
    
class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)
    tel = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.tel}"

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name
    
class Sell(models.Model):
    product = models.ForeignKey(Product, related_name="sells",on_delete=models.PROTECT)
    client = models.ForeignKey(Client, related_name="sells",on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name="sells", on_delete=models.PROTECT)
    def __str__(self):
        return self.product.name
class Destine(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    client = models.ForeignKey(Client, related_name="payments",on_delete=models.PROTECT, null=True, blank=True)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name="payments", on_delete=models.PROTECT)
    from_destine = models.ForeignKey(Destine, related_name="payments",on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return f"{self.client} {self.from_destine}"
    


class Expense(models.Model):
    destine = models.ForeignKey(Destine, related_name="expends", on_delete=models.PROTECT)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name="expends", on_delete=models.PROTECT)



class SellPaymentExpense:
    
    def __init__(self, obj):
        self.id = obj.id
        if hasattr(obj, 'product'):
            self.product = obj.product
        else:
            self.product = None

        if hasattr(obj, 'client'):
            self.client = obj.client
        else:
            self.client = None

        if hasattr(obj, 'quantity'):
            self.quantity = obj.quantity
        else:
            self.quantity = None

        if hasattr(obj, 'price'):
            self.price = obj.price
        else:
            self.price = None

        if hasattr(obj, 'date'):
            self.date = obj.date
        else:
            self.date = None

        if hasattr(obj, 'customer'):
            self.customer = obj.customer
        else:
            self.customer = None

        if hasattr(obj, 'destine'):
            self.destine = obj.destine
        else:
            self.destine = None

        if hasattr(obj, 'from_destine'):
            self.from_destine = obj.from_destine
            self.operation = "refund"
        else:
            self.from_destine = None

        if hasattr(obj, 'destine'):
            self.operation = "expense"
        elif hasattr(obj, 'quantity'):
            self.operation = "production"
        else:
            self.operation = "payment"

        if hasattr(obj, 'value'):
            self.value = obj.value
        else:
            self.value = None
    