import mammoth
from pprint import pprint
from rest_framework import serializers
from django.db.transaction import atomic
from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.apps import apps
from django.conf import settings
from .models import City,Airline, Enquire,Flight
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

from django.core.mail import send_mail

class CitySerializer(serializers.ModelSerializer): 
   
    class Meta:
        model = City
        fields = ['name']
    
class AirlineSerializer(serializers.ModelSerializer): 
   
    class Meta:
        model = Airline
        fields = ['name']


class FlightSerializer(serializers.ModelSerializer): 
    city = CitySerializer()
    city_to = CitySerializer()
    airline = AirlineSerializer()
    class Meta:
        model = Flight
        fields = ['id','final_price', 'airline','city','city_to', "date"]

    




class EnquireSerializer(serializers.ModelSerializer): 
    flight = FlightSerializer()
    class Meta:
        model = Enquire
        fields = ['contact', 'flight','status']


class EnquireCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enquire
        fields = [
            "id",
            "contact",
            "flight",
        ]

    def create(self, validate_data):

            email = "dulxeslopes16@gmail.com"
            subject = f'Ligue para {validate_data["contact"]}'
            flight = validate_data["flight"]
            message = f'Pretende viajar em {flight.date}, na {flight.airline.name} e custa {flight.final_price} dbs'
            from_email = 'edmilbe@gmail.com'  # Replace with your email address
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            # return render(request, 'email_sent.html')  # Render a success template


        
            return super().create(validate_data)
    
        
        
      

        

