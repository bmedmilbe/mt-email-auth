from django.conf import settings
from django.db import models

# Create your models here.

class Customer(models.Model):
    boss = models.BooleanField(default=False)
    is_deliver = models.BooleanField(default=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="troca_customer")
    def __str__(self):
        return self.user.first_name
class Friend(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name
    
class FriendPayment(models.Model):
    friend = models.ForeignKey(Friend, related_name="payments", on_delete=models.PROTECT)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    boss = models.ForeignKey(Customer, related_name="friend_payments", on_delete=models.PROTECT)
    description = models.CharField(max_length=255, null=True, blank=True)




class Transaction(models.Model):
    description = models.CharField(max_length=255)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    boss = models.ForeignKey(Customer, related_name="boss_transactions", on_delete=models.PROTECT)

    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    completed_by = models.ForeignKey(Customer, related_name="deliver_transactions", on_delete=models.PROTECT, null=True, blank=True)

    friend = models.ForeignKey(Friend, null=True,blank=True, related_name="transactions", on_delete=models.SET_NULL)
    friend_paid = models.BooleanField(default=False)
    is_charge = models.BooleanField(default=False)

class Charge(models.Model):
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    boss = models.ForeignKey(Customer, related_name="boss_charges",on_delete=models.PROTECT)
    deliver = models.ForeignKey(Customer, related_name="deliver_charges", on_delete=models.PROTECT)

