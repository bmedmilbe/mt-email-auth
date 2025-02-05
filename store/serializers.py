from pprint import pprint
from datetime import date, timedelta
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from templated_mail.mail import BaseEmailMessage
from django.db.transaction import atomic
import os
from django.core.mail import BadHeaderError
from django.apps import apps
from django.core.validators import MinValueValidator
from django.db.transaction import atomic
from decimal import Decimal
from django.conf import settings
# from . import helpers
import requests
import json
from . import models

class ColorSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = models.Color
        fields = ['id','name', 'hexcolor']

class ColorSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = models.Color
        fields = ['id','name', 'hexcolor']

class ProductImageSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    class Meta():
        model = models.ProductImage
        fields = ['id','color', 'image']
    
class IdentitySerializer(serializers.ModelSerializer):
    class Meta():
        model = models.Identity
        fields = ['id', 'name', 'slug']

class MatchSerializer(serializers.ModelSerializer):
    identity = IdentitySerializer()
    class Meta():
        model = models.Match
        fields = [ 'id','identity']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    matches = MatchSerializer(many=True)
    class Meta():
        model = models.Product
        fields = ['id','name', 'slug', 'price', 'description', 'images', 'matches']

class IdentityFirstProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    class Meta():
        model = models.Product
        fields = ['id','name', 'slug', 'price', 'description', 'images']


class IdentityFirstMatchSerializer(serializers.ModelSerializer):
    product = IdentityFirstProductSerializer()
    class Meta():
        model = models.Match
        fields = ['id','product']

class IdentityFirstSerializer(serializers.ModelSerializer):
    matches = IdentityFirstMatchSerializer(many=True)
    class Meta():
        model = models.Identity
        fields = ['id','name', 'slug','matches']



class  OrderFirstProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    class Meta():
        model = models.Product
        fields = ['id','name', 'slug', 'price', 'description', 'images']

class OrderFirstProductImageSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    product = OrderFirstProductSerializer()
    class Meta():
        model = models.ProductImage
        fields = ['id','color', 'image', "product"]

class OrderFirstSerializer(serializers.ModelSerializer):
    image = OrderFirstProductImageSerializer()
    class Meta():
        model = models.Order
        fields = ['id','image', 'quantity', "total", "customer", 'reference', 'created_at', 'is_paid', 'is_delivered']


class OrderCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    # customer = Order(read_only=True)
    reference = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    is_paid = serializers.CharField(read_only=True)
    is_delivered = serializers.CharField(read_only=True)
    total = serializers.IntegerField(read_only=True)

    class Meta():
        model = models.Order
        
        
        fields = ['id', "image", "quantity", 'total','customer',
                  'reference', 'created_at', 'is_paid', 'is_delivered']


    def create(self, validated_data):

        data = validated_data
        data['total'] = validated_data['quantity'] * validated_data['image'].product.price
        data['reference'] = "ruy6546o"
        data['customer_id'] = "1"

        return super().create(data)