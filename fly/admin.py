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
from io import BytesIO
from boto3.session import Session
import hashlib
from openpyxl import Workbook
import boto3
from cryptography.fernet import Fernet
from decimal import Decimal
from django.db.models import Count, ExpressionWrapper
from . import models
from . models import Flight, Airport
from django.conf import settings
from django.db.models import Q
import os
# Register your models here.

@admin.register(models.Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ["date","file"]
    def save_model(self, request, obj, form, change):

        # session = Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        #           aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

        #     # s3_client = session.client('s3')
        # s3_resource = session.resource('s3')
        # my_bucket = s3_resource.Bucket(settings.AWS_STORAGE_BUCKET_NAME)

        # pprint(settings.BASE_DIR)
        # my_bucket.download_file(obj.file.name,settings.BASE_DIR )

        # response = my_bucket.delete_objects(
        #         Delete={
        #             'Objects': [
        #                 {
        #                     'Key': f"{obj.file.name}"   # the_name of_your_file
        #                 }
        #             ]
        #         }
        #     )
        super().save_model(request, obj, form, change)

        # obj.save()
        months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        columns = ["a", "b", "c", "d", "e", "f", "g"]


        portugal_airports = list(Airport.objects.filter(country__acronym="PT"))
        rest_airports = list(Airport.objects.filter(~Q(country__acronym="PT")))
        routes = list()
        for portugal_airport in portugal_airports:
            for rest_airport in rest_airports:
                routes.append(f"{portugal_airport.acronym}-{rest_airport.acronym}".upper())
                routes.append(f"{rest_airport.acronym}-{portugal_airport.acronym}".upper())
        

        

        prices = dict()
        url = obj.file.url
        
        if obj.file.url != None:
            docx = BytesIO(requests.get(url).content)
            # Write the stuff
            with open("flights.xlsx", "wb") as f:
                f.write(docx.getbuffer())
                # pprint(docx)
                # pass
            workbook = load_workbook(filename="flights.xlsx")

            # routes = list()
            # for portugal_airport in portugal_airports:
            #     for rest_airport in rest_airports:
            #         # pprint(f"{portugal_airport.acronym}-{rest_airport.acronym}".upper())
            #         routes.append(f"{portugal_airport.acronym}-{rest_airport.acronym}".upper())
            #         routes.append(f"{rest_airport.acronym}-{portugal_airport.acronym}".upper())
                    # workbook.create_sheet(f"{portugal_airport.acronym}-{rest_airport.acronym}".upper())
                    # workbook.create_sheet(f"{rest_airport.acronym}-{portugal_airport.acronym}".upper())       
                # workbook.save('flights.xlsx')
            
            
            # workbook = load_workbook(filename=obj.file.url)
            
            for route in routes:
                sheet = workbook[route]
                current_month = None
                month_group = None
                year = None
                month_dict = dict()
                for row in range(1, sheet.max_row+1):
                    for column in columns:
                        # pprint(sheet)
                        cell = sheet[f"{column}{row}"].value
                        if cell:
                            if "MAIS" in str(cell).upper():
                                counter = 0
                                for month in months:
                                    counter = counter + 1
                                    if month.upper() in cell.upper():
                                        current_month = counter
                                        break
                            if month_group != months[current_month-1].upper():
                                month_group = months[current_month-1].upper()
                                # pprint(f"{month_group}")
                                month_dict[month_group] = list()

                            price = None
                            day = str(cell).replace("\n", " ").replace("  ", " ")
                            if "EURMAIS" in day.upper():
                                if year != day.split(" ")[1]:
                                    year = day.split(" ")[1]
                                    # price[year] = list()
                                break
                            elif " EUR" in day.upper():
                                cell_contents = day.split(" ")
                                day = cell_contents[0] if cell_contents[0].isnumeric() else None
                                price = cell_contents[1]
                            else:
                                day = day.split(" ")[0]
                            
                            
                            if price:
                                date = f'{year}-{current_month}-{(day)}'
                                month_dict[month_group].append({f"date":f'{year}-{current_month}-{(day)}',f"price":price })
                                # pprint(f"{year}-{current_month}-{(day)}: {price if price != None else 'NO FLY'}")
                                # pprint(Decimal(float(price.replace(",", "."))))
                                # return 1
                                price = Decimal(float(price.replace(".", "").replace(",", ".")))
                                # return 1
                                try:
                                    flight = Flight.objects.get(route =route, date=date)
                                    flight.price=price
                                    # pprint(price)
                                    flight.save()
                                    
                    
                                except Flight.DoesNotExist:
                                    Flight.objects.create(
                                        date=date,
                                        price=price,
                                        route =route
                                    )
                                                                
                    # pprint(month_dict)
                
                # pprint(obj.file.url)
                # conn = S3Connection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)
                # bucket_name = 'bm-edmilbe-bucket'
                # file_key = 'fly/flight/flight.xlsx'

                # bucket = Bucket(conn, bucket_name)
                # k = Key(bucket=bucket, name=file_key)
                # k.delete()
                # os.remove(obj.file.url)
                # obj.file.delete()
                # os.remove(os.path.join(settings.MEDIA_ROOT,f"{obj.file.name}"))



                

                # s3 = boto3.client('s3')
                # s3.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME,name=settings.AWS_SECRET_ACCESS_KEY, name=f"{obj.file.name}")
            # obj.save()
@admin.register(models.Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ["route","date", "price"]
    list_filter = ["route"]

@admin.register(models.Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ["acronym","name", "country"]
    # list_filter = ["country"]

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["acronym","name",]
@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ["name","message","flight"]
                    