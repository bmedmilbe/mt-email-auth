from django.contrib import admin
from .models import Payment, Person, Reference, Trush
from django.db.models import Count
# Register your models here.
from io import BytesIO, StringIO
import docx2txt
import requests
from pprint import pprint
import re
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "nike", "currency", "value", "payment_day","total"]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(total_referenced=Count("all_references"))

    def total(self, obj):
        return obj.total_referenced
    
    def save_model(self, request, obj, form, change):

        
        super().save_model(request, obj, form, change)

        # obj.save()
        months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        columns = ["a", "b", "c", "d", "e", "f", "g"]

        months = ["TAP", "TAAG"]

        exists = list()
        city_from = obj.city_from.id
        city_to = obj.city_to.id
        airlines = ["TAP", "TAAG", "EuroAtlantic", "Royal", "Qatar", "LAM"]
        if obj.file.url != None:
            txt_obj = BytesIO(requests.get(obj.file.url).content)
            all_data = f"{docx2txt.process(txt_obj)}".replace("\r","").replace("\n","").replace(" ", "").replace(";'>+","+").replace('</span></div></div></div>'," ")
            
            
            # Flight.objects.filter(city_id=city_from, city_to_id=city_to).delete()
            airline = None
            count = -1
            words = all_data.split(" ")
       
                
            for word in words:
                pprint(word)

                        # count = count + 1
                        
                        # if word in airlines:
                        #     airline = word

                        # if "/" in word:
                        #     date = word.split("/")
                            
                        #     day = date[0] if int(date[0]) > 9 else f"0{date[0]}"
                        #     month = date[1] if int(date[1]) > 9 else f"0{date[1]}"
                        #     time = words[count+1]
                        #     date = f"2024-{month}-{day} {time}"
                        
                        # if airline != None and word.startswith("€"):
                            
                        #     price = (int(word.replace("€","").replace(",","")) + 15)
                        #     # price = (int(word.replace("€","").replace(",","")) + 70) * 27
                        #     if city_from == 1:
                        #          price = (int(word.replace("€","").replace(",","")) + 32) * 27
                        #     # airline_id = 1 if airline == "TAP" else 2
                        #     airline_id = Airline.objects.filter(name__istartswith=airline).first().id
                            
                        #     if date not in exists:
                        #             exists.append(date)
                                
                        #             flight = Flight.objects.filter(
                                            
                        #                     airline_id=airline_id,
                        #                     # date__year=2024,
                        #                     # date__month=month,
                        #                     # date__day=day,
                        #                     date=date,
                        #                     city_id=city_from, 
                        #                     city_to_id=city_to,
                        #             )

                        #             if flight.exists():
                        #                  flight = flight.first()
                        #                  flight.final_price=price
                        #                  flight.base_price = int(word.replace("€","").replace(",",""))
                                        
                        #                  flight.save()
                        #             else:
                        #                 Flight.objects.create(
                        #                     final_price=price,
                        #                     airline_id=airline_id,
                        #                     date=date,city_id=city_from, 
                        #                     city_to_id=city_to,
                        #                     base_price = int(word.replace("€","").replace(",",""))
                        #                     )  
                        #     airline = None
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

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ["referenced_by","person"]
    
@admin.register(Trush)
class TrushAdmin(admin.ModelAdmin):
    list_display = ["date"]

    def save_model(self, request, obj, form, change):

        
        super().save_model(request, obj, form, change)

        # obj.save()
        months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        columns = ["a", "b", "c", "d", "e", "f", "g"]

        months = ["TAP", "TAAG"]

        exists = list()
        
        airlines = ["TAP", "TAAG", "EuroAtlantic", "Royal", "Qatar", "LAM"]
        if obj.file.url != None:
            txt_obj = BytesIO(requests.get(obj.file.url).content)
            all_data = f"{docx2txt.process(txt_obj)}".replace("\r","").replace("\n","").replace(" ", "").replace(';">+'," ").replace('</span></div></div></div>'," ")
            
            
            # Flight.objects.filter(city_id=city_from, city_to_id=city_to).delete()
            airline = None
            count = -1
            words = all_data.split(" ")
       
            numbers = list()
            for word in words:
                if word.isnumeric():
                    numbers.append(f"+{word}")
            

            pprint(len(numbers))


                        # count = count + 1
                        
                        # if word in airlines:
                        #     airline = word

                        # if "/" in word:
                        #     date = word.split("/")
                            
                        #     day = date[0] if int(date[0]) > 9 else f"0{date[0]}"
                        #     month = date[1] if int(date[1]) > 9 else f"0{date[1]}"
                        #     time = words[count+1]
                        #     date = f"2024-{month}-{day} {time}"
                        
                        # if airline != None and word.startswith("€"):
                            
                        #     price = (int(word.replace("€","").replace(",","")) + 15)
                        #     # price = (int(word.replace("€","").replace(",","")) + 70) * 27
                        #     if city_from == 1:
                        #          price = (int(word.replace("€","").replace(",","")) + 32) * 27
                        #     # airline_id = 1 if airline == "TAP" else 2
                        #     airline_id = Airline.objects.filter(name__istartswith=airline).first().id
                            
                        #     if date not in exists:
                        #             exists.append(date)
                                
                        #             flight = Flight.objects.filter(
                                            
                        #                     airline_id=airline_id,
                        #                     # date__year=2024,
                        #                     # date__month=month,
                        #                     # date__day=day,
                        #                     date=date,
                        #                     city_id=city_from, 
                        #                     city_to_id=city_to,
                        #             )

                        #             if flight.exists():
                        #                  flight = flight.first()
                        #                  flight.final_price=price
                        #                  flight.base_price = int(word.replace("€","").replace(",",""))
                                        
                        #                  flight.save()
                        #             else:
                        #                 Flight.objects.create(
                        #                     final_price=price,
                        #                     airline_id=airline_id,
                        #                     date=date,city_id=city_from, 
                        #                     city_to_id=city_to,
                        #                     base_price = int(word.replace("€","").replace(",",""))
                        #                     )  
                        #     airline = None
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


