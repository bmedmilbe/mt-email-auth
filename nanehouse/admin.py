from datetime import datetime
from django.contrib import admin, messages
from django.http import HttpRequest
from pprint import pprint
from django.utils.html import format_html
from django.utils.http import urlencode
from django.urls import reverse
# Import pandas
# from openpyxl import load_workbook
# import pandas as pd
from django.core.files import File
from . import helpers
import requests
from io import BytesIO
import hashlib
# from openpyxl import Workbook

from cryptography.fernet import Fernet

from django.db.models import Count, ExpressionWrapper
from . import models
from django.conf import settings

class HouseImageInline(admin.TabularInline):
    model = models.HouseImage

class CityInline(admin.TabularInline):
    model = models.City

class CountryInline(admin.TabularInline):
    model = models.Country




@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}  # new
    search_fields = ["name"]
@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    prepopulated_fields = {"slug": ("name",)}  # new
    search_fields = ["name"]
    list_editable = ["country"]


@admin.register(models.Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ["name", "city"]
    prepopulated_fields = {"slug": ("name",)}  # new
    search_fields = ["name"]
    list_editable = ["city"]





@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["street", "price_for_nane", 'price_rent', 'price_sell', "type", "active"]
    prepopulated_fields = {"slug": ("type","number", "street")}  # new

    autocomplete_fields = ["street", "owner"]
    search_fields = ["street"]

    list_per_page = 15
    ordering = ["street"]
    list_editable = ['price_for_nane', 'price_sell','price_rent', "type", "active"]

    inlines = [HouseImageInline]

    # def images_counts(self, product: models.Product):
    #     return product.images.count()

    # def get_queryset(self, request: HttpRequest):
    #     return super().get_queryset(request).annotate(image_count=Count("images"))


# @admin.register(models.ProductShop)
# class ProductShopAdmin(admin.ModelAdmin):
#     list_display = ["name", "price", "store"]
#     prepopulated_fields = {"slug": ("product", "shop")}  # new
#     autocomplete_fields = ["shop", "product"]

#     search_fields = ["product__name"]
#     list_per_page = 10
#     ordering = ["product__name"]
#     list_editable = ["price"]

#     def store(self, product_shop: models.ProductShop):
#         return shop.name

#     def name(self, product_shop: models.ProductShop):
#         return product.name


@admin.register(models.HouseImage)
class HouseImageAdmin(admin.ModelAdmin):

    list_display = ["id"]
    # list_editable = ["image"]
    # autocomplete_fields = ['product']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name"]

    search_fields = ["user__first_name__istartswith",
                     "user__last_name__istartswith"]
    # list_editable = ["seller"]
    list_per_page = 10
    ordering = ["user__first_name"]

    def name(self, customer: models.Customer):
        return f'{customer.user.first_name} {customer.user.last_name}'

   

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "country"]
    search_fields = ["first_name__istartswith", "last_name__istartswith"]
    # list_editable = ["seller"]
    list_per_page = 15
    ordering = ["first_name"]

    def name(self, customer: models.Customer):
        return f'{customer.user.first_name} {customer.user.last_name}'

    # def orders(self, customer: models.Customer):
    #     return customer.orders.count()

    # def stores(self, customer: models.Customer):
    #     return customer.stores.count()

    # def addresses(self, customer: models.Customer):
    #     return customer.addresses

    # def get_queryset(self, request: HttpRequest):
    #     return super().get_queryset(request).annotate(addresses=Count("address"))


    # def account(self, customer: models.Customer):
    #     return f'{customer.name_in_bank} | {customer.sort_code} | {customer.account_number}'

    # def total_in_sales(self, customer: models.Customer):
    #     total_spent = 0
    #     for item in customer.product_set.all():
    #         for orderitem in item.orderitems.all():
    #             total_spent = total_spent + orderitem.price * orderitem.quantity

    #     return f'{total_spent:.2f}'

    # def pay_back(self, customer: models.Customer):
    #     total_paid = 0

    #     for payment in customer.payments.all():
    #         total_paid = total_paid + payment.amount

    #     return f'{total_paid:.2f}'

   

    

    # def products(self, customer: models.Customer):
    #     return f'{customer.product.count()} items'

    # def get_queryset(self, request: HttpRequest):
    #     return super().get_queryset(request)

@admin.register(models.ClientHouse)
class ClientHouseAdmin(admin.ModelAdmin):
    list_display = ["client", "house"]
    list_per_page = 15
    ordering = ["client"]
    search_fields = ['client']


@admin.register(models.ClientPayment)
class ClientPaymentAdmin(admin.ModelAdmin):
    list_display = ["client", "value"]
    list_per_page = 15
    ordering = ["client"]
    search_fields = ['client']

@admin.register(models.OwnerPayment)
class OwnerPaymentAdmin(admin.ModelAdmin):
    list_display = ["owner", "value"]
    list_per_page = 15
    ordering = ["owner"]
    search_fields = ['owner']

