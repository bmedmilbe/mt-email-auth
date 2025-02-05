from django.contrib import admin
from . import models
import re
# Register your models here.
from pprint import pprint
class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    autocomplete_fields = ['color']
    


class MatchInline(admin.TabularInline):
    model = models.Match
    autocomplete_fields = ['identity']


def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s

@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'hexcolor']
    list_editable = ['hexcolor']
    search_fields = ['name']

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'price_off']
    prepopulated_fields = {'slug': ['name']}
    list_editable = ['price', 'price_off']
    search_fields = ['name']
    autocomplete_fields = ['category']

    inlines = [ProductImageInline, MatchInline]

@admin.register(models.Identity)
class IdentityAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name']

    def get_queryset(self, request):


        # with open('new_new.txt','r') as r:
        #     for data in r:
        #         if "Google" in data or "Oppo" in data:
        #             data = data.replace("\n", '')
        #             models.Identity.objects.create(name=data, slug=slugify(data.replace("+"," plus")))

        return super().get_queryset(request)


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['product']
    list_filter = ['identity']



@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'color']
    autocomplete_fields = ['product', 'color']
    search_fields = ["product"]

@admin.register(models.OrderCustomer)
class OrderCustomerAdmin(admin.ModelAdmin):
    list_display = ['phone','name']

    search_fields = ['name', 'phone']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','reference', 'is_paid', 'is_delivered']
    list_filter = ['customer', 'is_paid', 'is_delivered']
    autocomplete_fields =['image', 'customer']

@admin.register(models.OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['order','status']
    list_filter = ['order']



    
