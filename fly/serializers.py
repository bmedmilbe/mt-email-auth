import mammoth
from pprint import pprint
from rest_framework import serializers
from django.db.transaction import atomic
from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.apps import apps
from django.conf import settings
from .models import  Airport, Flight, Country, Request
from core.serializers import UserCreateSerializer
from django.core.files import File
import timeago
from datetime import datetime, timezone
from io import BytesIO
import docx2txt
import re
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection, send_mail

class CountrySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Country
        fields = ['id', 'acronym', 'name', 'image']

class AirportSerializer(serializers.ModelSerializer): 
    country =  CountrySerializer()
    class Meta:
        model = Airport
        fields = ['id', 'country', 'acronym', 'name', 'image']

class FlightSerializer(serializers.ModelSerializer):
    # airport = AirportSerializer()
    

    country_from = serializers.SerializerMethodField(
        method_name="get_country_from")
    country_to = serializers.SerializerMethodField(
        method_name="get_country_to")
    class Meta:
        model = Flight
        fields = ['id','date', 'price', 'route', 'country_from', 'country_to']

    def get_country_from(self, obj):
        
        acronym = obj.route.split("-")[0]
        airport = Airport.objects.get(acronym=acronym)
        serializer = CountrySerializer(airport.country)
        return serializer.data
    def get_country_to(self, obj):
       
        acronym = obj.route.split("-")[1]
        airport = Airport.objects.get(acronym=acronym)
        serializer = CountrySerializer(airport.country)
        return serializer.data
    
class CountryWithAirportsSerializer(serializers.ModelSerializer): 
    airports = AirportSerializer(many=True)
    class Meta:
        model = Country
        fields = ['id','acronym','name','airports', 'image']



class RequestCreatSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Request
        fields = ['name','flight','contact','message']

