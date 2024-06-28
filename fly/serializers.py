import mammoth
from pprint import pprint
from rest_framework import serializers
from django.db.transaction import atomic
from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.apps import apps
from django.conf import settings
from .models import  Contact, Enquire
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

    class Meta:
        model = Enquire
        fields = ['country','depart_date','return_date', 'contact_detail']

    def create(self, validated_data):
        
        contacts = Contact.objects.filter(contact=validated_data['contact_detail'])
        
        contact = contacts.first()
        if contact == None:
            contact = Contact.objects.create(contact=validated_data["contact_detail"])
        
        
        country = validated_data["country"]
        depart_date = validated_data["depart_date"]
        return_date = validated_data["return_date"]

        Enquire.objects.create(contact_id=contact.id, depart_date=depart_date, return_date=return_date, country=country)
        return {**validated_data}

        

