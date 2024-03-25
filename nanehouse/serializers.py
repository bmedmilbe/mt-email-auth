from dataclasses import fields

from pprint import pprint
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.core.validators import MinValueValidator
from django.db.transaction import atomic
from decimal import Decimal
from django.conf import settings
from django.db.models.aggregates import Count
from cryptography.fernet import Fernet
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import random
from django.contrib.auth.hashers import check_password
import requests
import json
from django.db.models import Q
from .models import (
    City,
    Currency,
    Customer,
    Country,
    House,
    HouseImage,
    Street,
)
from django.db.models import Sum
from django.db.transaction import atomic

import re


def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            "id",
            "name",
        ]

class CountrySerializer(ModelSerializer):
    currency = CurrencySerializer()
    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "currency"
        ]

class CitySerializer(ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "country"
        ]

class StreetSerializer(ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Street
        fields = [
            "id",
            "name",
            "city"
        ]
class HouseImageSerializer(ModelSerializer):
    class Meta:
        model = HouseImage
        fields = [
            "id",
            "image",
        ]

class HouseSerializer(ModelSerializer):
   
    images = HouseImageSerializer(many=True)
    street = StreetSerializer()


    class Meta:
        model = House
        fields = [
            "id",
            "number",
            "street",
            'price_sell',
            "price_rent",
            "rooms",
            "images",
            "description",
            "energy_level",
            "type",
           
        ]

    