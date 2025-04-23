from django.contrib import admin
from .models import Customer, Client, Destine, Expense, Payment,Product, Sell


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user']

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'tel']
    search_fields = ['name']
@admin.register(Destine)
class DestineAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields=['name']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['destine', 'value']


@admin.register(Sell)
class SellAdmin(admin.ModelAdmin):
    list_display = ['product','client', 'quantity','price', 'date']
    list_editable = ['client', 'quantity','price']
    list_filter = ['product','client']
    autocomplete_fields = ['client', 'product']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['value','client', 'date']
    list_filter = ['client']
    autocomplete_fields = ['client', 'from_destine']


   