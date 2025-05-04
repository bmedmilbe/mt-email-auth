from django.contrib import admin

from .models import Charge, Friend, Customer, FriendPayment, Transaction

# Register your models here.
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(FriendPayment)
class FriendPaymentAdmin(admin.ModelAdmin):
    list_display = ['friend','value']
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','boss']
    list_editable = ['boss']

@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ['value','boss', 'deliver']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['value','description', 'friend', 'completed_by','completed', 'friend_paid', 'date', 'is_charge']
    list_filter = ['completed', 'friend_paid', 'is_charge','completed_by', 'boss']
    list_editable = [ 'completed', 'friend_paid','friend', 'completed_by']
    search_fields = ['description', 'value']


   