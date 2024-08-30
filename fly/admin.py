from datetime import datetime
from django.contrib import admin, messages
from django.http import HttpRequest
from pprint import pprint
from django.utils.html import format_html
from django.utils.http import urlencode
from django.urls import reverse
# Import pandas
from openpyxl import load_workbook
from django.core.files import File
import requests
from io import BytesIO, StringIO
from boto3.session import Session
import hashlib
import docx2txt

from openpyxl import Workbook
import boto3
from cryptography.fernet import Fernet
from decimal import Decimal
from django.db.models import Count, ExpressionWrapper
from . import models
from . models import Flight
from django.conf import settings
from django.db.models import Q
import os
# Register your models here.

@admin.register(models.Trush)
class TrushAdmin(admin.ModelAdmin):
    list_display = ["date"]
    def save_model(self, request, obj, form, change):

        
        super().save_model(request, obj, form, change)

        # obj.save()
        months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        columns = ["a", "b", "c", "d", "e", "f", "g"]

        months = ["TAP", "TAAG"]

        exists = list()
        if obj.file.url != None:
            txt_obj = BytesIO(requests.get(obj.file.url).content)
            all_data = f"{docx2txt.process(txt_obj)}".replace("\r"," ").replace("\n"," ").replace("  ", " ")
            Flight.objects.all().delete()
            airline = None
            count = -1
            words = all_data.split(" ")
            for word in words:
                        count = count + 1
                        
                        if word == "TAP" or word == "TAAG":
                            airline = word

                        
                        if "/" in word:
                            date = word.split("/")
                            
                            day = date[0] if int(date[0]) > 9 else f"0{date[0]}"
                            month = date[1] if int(date[1]) > 9 else f"0{date[1]}"
                            time = words[count+1]
                            date = f"2024-{month}-{day} {time}"
                        
                        if airline != None and word.startswith("€"):
                            price = (int(word.replace("€","").replace(",","")) + 32) * 27
                            airline_id = 1 if airline == "TAP" else 2
                            
                            if date not in exists:
                                    exists.append(date)
                                
                                    flight = Flight.objects.filter(
                                            
                                            airline_id=airline_id,
                                            date__year=2024,
                                            date__month=month,
                                            date__day=day,
                                            city_id=1, 
                                            city_to_id=2,
                                    )

                                    if flight.exists():
                                         flight = flight.first()
                                         flight.final_price=price
                                         flight.base_price = int(word.replace("€","").replace(",",""))
                                        
                                         flight.save()
                                    else:
                                        Flight.objects.create(
                                            final_price=price,
                                            airline_id=airline_id,
                                            date=date,city_id=1, 
                                            city_to_id=2,
                                            base_price = int(word.replace("€","").replace(",",""))
                                            )  
                            airline = None
                        # print(word)
                # ... read the file ...
                # file.close()
        # if obj.file.url != None:

        #     with open(f"{file_name}", 'r') as file:
        #         Flight.objects.all().delete()
        #         airline = None
        #         for line in file:
        #             words = line.split()
        #             for word in words:
        #                 # Process each word
        #                 if word == "TAP" or word == "TAAG":
        #                     airline = word
                        
        #                 if "/" in word:
        #                     date = word.split("/")
        #                     day = date[0] if int(date[0]) > 9 else f"0{date[0]}"
        #                     month = date[1] if int(date[1]) > 9 else f"0{date[1]}"
        #                     date = f"2024-{month}-{day}"
                        
        #                 if airline != None and word.startswith("€"):
        #                     price = (int(word.replace("€","")) + 30) * 27
        #                     airline_id = 1 if airline == "TAP" else 2
        #                     Flight.objects.create(
        #                         final_price=price,
        #                         airline_id=airline_id,
        #                         date=date,city_id=1, 
        #                         city_to_id=2,
        #                         base_price = int(word.replace("€",""))
        #                         )
        #                     airline = None
        #                 print(word)
        #         # ... read the file ...
        #         file.close()

            # # extract text
            # text = docx2txt.process(txt)
            # pprint(text)
            # with open(obj.file.url, 'r') as file:
                
            #     airline = None
            #     for line in file:
            #         words = line.split()
            #         for word in words:
            #             # Process each word
            #             if word == "TAP" or word == "TAAG":
            #                 airline = word
                        
            #             if "/" in word:
            #                 date = word.split("/")
            #                 day = date[0] if int(date[0]) > 9 else f"0{date[0]}"
            #                 month = date[1] if int(date[1]) > 9 else f"0{date[1]}"
            #                 date = f"2024-{month}-{day}"
                        
            #             if airline != None and word.startswith("€"):
            #                 price = (int(word.replace("€","")) + 30) * 27
            #                 airline_id = 1 if airline == "TAP" else 2
            #                 Flight.objects.create(
            #                     final_price=price,
            #                     airline_id=airline_id,
            #                     date=date,city_id=1, 
            #                     city_to_id=2,
            #                     base_price = int(word.replace("€",""))
            #                     )
            #                 airline = None
            #             print(word)
            #     # ... read the file ...
            #     file.close()

@admin.register(models.Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ["id","name"]  

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id","name"] 

@admin.register(models.Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ["final_price", "airline", "date"] 
    ordering = ["final_price"] 
    list_filter = ["airline"]

@admin.register(models.Enquire)
class EnquireAdmin(admin.ModelAdmin):
    list_display = ["contact", "flight", "status"] 
    list_editable = ["status"]   

      

                

         
# @admin.register(models.Flight)
# class FlightAdmin(admin.ModelAdmin):
#     list_display = ["route","date", "price"]
#     list_filter = ["route"]

# @admin.register(models.Airport)
# class AirportAdmin(admin.ModelAdmin):
#     list_display = ["acronym","name", "country"]
#     # list_filter = ["country"]

# @admin.register(models.Country)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ["acronym","name",]


# @admin.register(models.Enquire)
# class RequestAdmin(admin.ModelAdmin):
#     list_display = ["contact","country","country_to","depart_date", "return_date", "base_price", "final_price", "paid","obs"]
#     list_editable = ["base_price", "final_price", "paid","obs"]
#     list_filter = ['contact']
# @admin.register(models.ContactOff)
# class RequestAdmin(admin.ModelAdmin):
#     list_display = ["contact","date"]
                    
