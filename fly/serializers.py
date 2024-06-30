import mammoth
from pprint import pprint
from rest_framework import serializers
from django.db.transaction import atomic
from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.apps import apps
from django.conf import settings
from .models import  Contact, Enquire, Country
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
from django.db.models import Q


class EnquireCreatSerializer(serializers.ModelSerializer): 
   
    contact_detail = serializers.CharField()
    country = serializers.CharField()
    country_to = serializers.CharField()


    class Meta:
        model = Enquire
        fields = ['country','country_to','depart_date','return_date', 'contact_detail']

    def create(self, validated_data):
        
        contacts = Contact.objects.filter(contact=validated_data['contact_detail'])
        
        contact = contacts.first()
        if contact == None:
            contact = Contact.objects.create(contact=validated_data["contact_detail"])

        countries = Country.objects.filter(name=validated_data['country'])
        
        country = countries.first()
        if country == None:
            country = Country.objects.create(name=validated_data["country"])


        countries = Country.objects.filter(name=validated_data['country_to'])
        
        country_to = countries.first()
        if country_to == None:
            country_to = Country.objects.create(name=validated_data["country_to"])
        
        
        # country = validated_data["country"]
        depart_date = validated_data["depart_date"]
        return_date = validated_data["return_date"]

        Enquire.objects.create(contact_id=contact.id, depart_date=depart_date, return_date=return_date, country_id=country.id, country_to_id=country_to.id)
        return {**validated_data}

        

