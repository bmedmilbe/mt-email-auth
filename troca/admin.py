from django.contrib import admin

from .models import Charge, Friend, Customer, Transaction

# Register your models here.
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ['name',]
    

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','boss']
    list_editable = ['boss']
@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ['value','boss', 'deliver']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['value','description', 'completed', 'friend_paid']
    list_filter = ['completed', 'friend_paid']
    list_editable = [ 'completed', 'friend_paid']

