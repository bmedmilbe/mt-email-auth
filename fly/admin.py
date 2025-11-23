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
from . models import Airline, Flight
from django.conf import settings
from django.db.models import Q
import os
# Register your models here.

@admin.register(models.Trush)
class TrushAdmin(admin.ModelAdmin):
    list_display = ["date", "city_from", "city_to"]
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
        # pprint(obj.file.url)

        if obj.file.url != None:
            txt_obj = BytesIO(requests.get(obj.file.url).content)
            # pprint(txt_obj)
            all_data = f"{docx2txt.process(txt_obj)}".replace("\r"," ").replace("\n"," ").replace("  ", " ")
            Flight.objects.filter(city_id=city_from, city_to_id=city_to).delete()
            
            airline = None
            count = -1
            words = all_data.split(" ")
            year = 2025
            date = "2023-05-04"
            pprint(words)
            for word in words:
                        
                        
                        count = count + 1
                        
                        if word in airlines:
                            airline = word

                        if "/" in word and len(word)>3:
                            date = word.split("/")
                            # pprint(word)
                            
                            day = date[0] if int(date[0]) > 9 else f"0{date[0]}"
                            month = date[1] if int(date[1]) > 9 else f"0{date[1]}"
                            time = words[count+1]
                            date = f"{year}-{month}-{day} {time}"
                        
                        if airline != None and word.startswith("€") and date != "2023-05-04":
                            
                            price = (int(word.replace("€","").replace(",","")) + 15)
                            # price = (int(word.replace("€","").replace(",","")) + 70) * 27
                            if city_from == 1:
                                 price = (int(word.replace("€","").replace(",","")) + 32) * 27
                            # airline_id = 1 if airline == "TAP" else 2
                            airline_id = Airline.objects.filter(name__istartswith=airline).first().id
                            
                            if date not in exists:
                                    exists.append(date)
                                
                                    flight = Flight.objects.filter(
                                            
                                            airline_id=airline_id,
                                            # date__year=2024,
                                            # date__month=month,
                                            # date__day=day,
                                            date=date,
                                            city_id=city_from, 
                                            city_to_id=city_to,
                                    )

                                    if flight.exists():
                                         flight = flight.first()
                                         flight.final_price=price
                                         flight.base_price = int(word.replace("€","").replace(",",""))
                                        
                                         flight.save()
                                    else:
                                        created = Flight.objects.create(
                                            final_price=price,
                                            airline_id=airline_id,
                                            date=date,
                                            city_id=city_from, 
                                            city_to_id=city_to,
                                            route_id = obj.id,
                                            base_price = int(word.replace("€","").replace(",",""))
                                            ) 
                                        # pprint(created) 
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

@admin.register(models.Country)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ["id","name"]  
@admin.register(models.Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ["id","name"]  

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id","name", "country"] 

@admin.register(models.Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ["final_price", "airline", "date", "city"] 
    ordering = ["final_price"] 
    list_filter = ["airline", "city"]

@admin.register(models.Enquire)
class EnquireAdmin(admin.ModelAdmin):
    list_display = ["contact", "flight", "status"] 
    list_editable = ["status"]   

# @admin.register(models.Users)
# class UsersAdmin(admin.ModelAdmin):
#     list_display = ["name"] 


# @admin.register(models.Moviments)
# class MovimentsAdmin(admin.ModelAdmin):
#     list_display = ["user","value","description", "date", "type"] 

#     list_filter = ["user", "type", "date"]



@admin.register(models.Menssenger)
class MenssengerAdmin(admin.ModelAdmin):
    list_display = ["id","file"]
    def save_model(self, request, obj, form, change):

        
        super().save_model(request, obj, form, change)

        # obj.save()
        months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        columns = ["a", "b", "c", "d", "e", "f", "g"]

        months = ["TAP", "TAAG"]

        exists = list()
        ins = """"""
        outs =""""""
        
        if obj.file.url != None:
            txt_obj = BytesIO(requests.get(obj.file.url).content)
            all_data = f"{docx2txt.process(txt_obj)}".replace("\r"," ").replace("\n"," ").replace("  ", " ").replace(",00.", "").replace(".,00", "")\
                .replace(",00", "")\
                .replace("Hamilton Lucas Gln","").replace("Faustina Martins Ramos","")
            
            

            count = -1
            words = all_data.split(" ")
            value = 0
            users = ["Hamilton","Faustina"]
            current_user =words[0]
            description = ""
            result = { 
                 users[0]: {
                 'in': 0,
                 'out': 0
            },
            users[1]:{
                 'in': 0,
                 'out': 0
            }}
            for word in words:
                if ".00" in word:
                    # pprint(word)
                    if word[-1] == "0" and word[-2] == "0" and word[-3] == ".":
                          word = word[:-3]

                    # pprint(word)

                if "." in word:
                    word = word.replace(".","")
                    # pprint(word)
                count = count + 1
                
                if word in users:
                     
                    if count > 1:
                        value = 0
                        for x in description.split(" "):
                             if x.isnumeric():
                                #   pprint(x)
                                if int(x) > 31:
                                    value = int(x)

                        result[current_user] = {
                         "in": result[current_user]['in'] + value if "RECEBI" in description.upper() else result[current_user]['in'],
                         "out": result[current_user]['out'] + value if "RECEBI" not in description.upper() else result[current_user]['out']
                         }
                        if 'RECEBI' in description.upper():
                            ins = f"""{ins}\n{value}"""
                        elif 'RECEBI' not in description.upper() and value > 0:
                            outs = f"""{outs}\n{value}"""

                        # pprint(f"{value} | {description}")
                             
                    current_user = word
                    description = ''
                else:
                     description = f"{description} {word}"
                     

            details = """"""
            # for user in users: 
            in_ = result[users[0]]['in']+result[users[1]]['in']
            out_ = result[users[0]]['out']+result[users[1]]['out']
            details = f"""Recebeu {in_}, entregou {out_}.\nSaldo:{in_-out_} (se foi entregue todo o valor anotado)\nCaso haja valor por entregar faça {out_} - (total de valores por entregar), porque esses valores ainda não foram entregue."""

            obj.details = f"{details} \nEntrada: {ins} \nSaida:{outs}" 
            # pprint(ins)
            # pprint(outs)

            super().save_model(request, obj, form, change)       
                     
                     



                     

@admin.register(models.Law)
class LawAdmin(admin.ModelAdmin):
    list_display = ["id","current_law"]
    def save_model(self, request, obj, form, change):

        
        super().save_model(request, obj, form, change)

        # obj.save()
        months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        columns = ["a", "b", "c", "d", "e", "f", "g"]

        months = ["TAP", "TAAG"]

        exists = list()
        ins = """"""
        outs =""""""
        
        if obj.current_law.url != None:
            txt_obj = BytesIO(requests.get(obj.current_law.url).content)
            all_data = f"{docx2txt.process(txt_obj)}".replace("- ","")\
            # .replace("\r"," ").replace("\n"," ")
            
            

            count = -1
            paragraphs = all_data.split("\n")
            # pprint(paragraph)

            paragraphs = [paragraph for paragraph in paragraphs if paragraph != ""]
            never = 0
            orgs = []
            art = cap = section = ssection = law = 0
            for paragraph in paragraphs:
                count = count + 1
                
                # pprint(paragraph)
                # return
                
                if paragraph.startswith("Artigo"):
                        #  pprint(paragraph)
                        never = count + 1
                        art = paragraph
                        orgs.append({"text":paragraph, "type": "A", "art": art })
                        orgs.append({"text":paragraphs[count+1], "type": "AN", "art": art })

                elif paragraph.startswith("CAPÍTULO"):
                        #  pprint(paragraph)
                        never = count + 1
                        cap = paragraph
                        orgs.append({"text":paragraph, "type": "C", "art": None, "cap": cap })
                        orgs.append({"text":paragraphs[count+1], "type": "CN", "art": None, "cap": cap })


                elif paragraph.startswith("SECÇÃO"):
                        #  pprint(paragraph)
                        never = count + 1
                        section = paragraph
                        orgs.append({"text":paragraph, "type": "S", "art": None, "section": section })
                        orgs.append({"text":paragraphs[count+1], "type": "SN", "art": None, "secction": section })


                elif paragraph.startswith("SUB-SECÇÃO"):
                        #  pprint(paragraph)
                        never = count + 1
                        ssection = paragraph
                        orgs.append({"text":paragraph, "type": "SS", "art": None, "sub_section": ssection })
                        orgs.append({"text":paragraphs[count+1], "type": "SSN", "art": None, "sub_secction": ssection })

                    
                elif paragraph.endswith("/2021"):
                        # pprint(paragraphs[count+1])
                        never = count + 1
                        law = paragraph
                        orgs.append({"text":paragraph, "type": "L", "art": None, "law": law })
                        orgs.append({"text":paragraphs[count+1], "type": "LN", "art": None, "law": law })

                elif paragraph.endswith(":"):
                        never = 0
                        # pprint(paragraphs[count])
                        text = paragraphs[count]
                        orgs.append({"text":text, "type": "P", "art": art, "law": law })
                
                elif count != never:
                    #  pprint(paragraph)
                     text = paragraphs[count]
                     orgs.append({"text":text, "type": "T", "art": art, "section": section, "sub_section": ssection,"cap":cap  })
                
                      
            for item in [org for org in orgs if org["type"] in ["SSN", "SN", "CN"]]:
                 pass
                #  pprint(item['text']) 
        orgs_1 = orgs
        orgs = []
        if obj.cv_code.url != None:
            txt_obj = BytesIO(requests.get(obj.cv_code.url).content)
            all_data = f"{docx2txt.process(txt_obj)}".replace("- ","")\
            # .replace("\r"," ").replace("\n"," ")
            
            

            count = -1
            paragraphs = all_data.split("\n")
            # pprint(paragraph)

            paragraphs = [paragraph for paragraph in paragraphs if paragraph != ""]
            never = 0
            art = cap = section = ssection = law = 0
            for paragraph in paragraphs:
                count = count + 1
                
                # pprint(paragraph)
                # return
                
                if paragraph.startswith("Artigo"):
                        #  pprint(paragraph)
                        never = count + 1
                        art = paragraph
                        orgs.append({"text":paragraph, "type": "A", "art": art })
                        orgs.append({"text":paragraphs[count+1], "type": "AN", "art": art })

                elif paragraph.startswith("CAPÍTULO"):
                        #  pprint(paragraph)
                        never = count + 1
                        cap = paragraph
                        orgs.append({"text":paragraph, "type": "C", "art": None, "cap": cap })
                        orgs.append({"text":paragraphs[count+1], "type": "CN", "art": None, "cap": cap })


                elif paragraph.startswith("SECÇÃO"):
                        #  pprint(paragraph)
                        never = count + 1
                        section = paragraph
                        orgs.append({"text":paragraph, "type": "S", "art": None, "section": section })
                        orgs.append({"text":paragraphs[count+1], "type": "SN", "art": None, "secction": section })


                elif paragraph.startswith("SUB-SECÇÃO"):
                        #  pprint(paragraph)
                        never = count + 1
                        ssection = paragraph
                        orgs.append({"text":paragraph, "type": "SS", "art": None, "sub_section": ssection })
                        orgs.append({"text":paragraphs[count+1], "type": "SSN", "art": None, "sub_secction": ssection })

                    
                elif paragraph.endswith("/2021"):
                        # pprint(paragraphs[count+1])
                        never = count + 1
                        law = paragraph
                        orgs.append({"text":paragraph, "type": "L", "art": None, "law": law })
                        orgs.append({"text":paragraphs[count+1], "type": "LN", "art": None, "law": law })

                elif paragraph.endswith(":"):
                        never = 0
                        # pprint(paragraphs[count])
                        text = paragraphs[count]
                        orgs.append({"text":text, "type": "P", "art": art, "law": law })
                
                elif count != never:
                    #  pprint(paragraph)
                     text = paragraphs[count]
                     orgs.append({"text":text, "type": "T", "art": art, "section": section, "sub_section": ssection,"cap":cap  })
                
                      
            for item in [org for org in orgs if org["type"] in ["SSN", "SN", "CN"]]:
                #  pprint(item['text']) 
                #  pprint(''.join(sorted(item['text'].lower())).replace(" ","").replace(",",""))
                pass
                      
        orgs_2 = orgs
        orgs = []     
        if obj.new_code.url != None:
            txt_obj = BytesIO(requests.get(obj.new_code.url).content)
            all_data = f"{docx2txt.process(txt_obj)}".replace("- ","")\
            # .replace("\r"," ").replace("\n"," ")
            

            count = -1
            paragraphs = all_data.split("\n")
            # pprint(paragraph)

            paragraphs = [paragraph for paragraph in paragraphs if paragraph != ""]
            never = 0
            art = cap = section = ssection = law = 0
            for paragraph in paragraphs:
                count = count + 1
                
                # pprint(paragraph)
                # return
                
                if paragraph.startswith("Artigo"):
                        #  pprint(paragraph)
                        never = count + 1
                        art = paragraph
                        orgs.append({"text":paragraph, "type": "A", "art": art })
                        orgs.append({"text":paragraphs[count+1], "type": "AN", "art": art })

                elif paragraph.startswith("CAPÍTULO"):
                        #  pprint(paragraph)
                        never = count + 1
                        cap = paragraph
                        orgs.append({"text":paragraph, "type": "C", "art": None, "cap": cap })
                        orgs.append({"text":paragraphs[count+1], "type": "CN", "art": None, "cap": cap })


                elif paragraph.startswith("SECÇÃO"):
                        #  pprint(paragraph)
                        never = count + 1
                        section = paragraph
                        orgs.append({"text":paragraph, "type": "S", "art": None, "section": section })
                        orgs.append({"text":paragraphs[count+1], "type": "SN", "art": None, "secction": section })


                elif paragraph.startswith("SUB-SECÇÃO"):
                        #  pprint(paragraph)
                        never = count + 1
                        ssection = paragraph
                        orgs.append({"text":paragraph, "type": "SS", "art": None, "sub_section": ssection })
                        orgs.append({"text":paragraphs[count+1], "type": "SSN", "art": None, "sub_secction": ssection })

                    
                elif paragraph.endswith("/2021"):
                        # pprint(paragraphs[count+1])
                        never = count + 1
                        law = paragraph
                        orgs.append({"text":paragraph, "type": "L", "art": None, "law": law })
                        orgs.append({"text":paragraphs[count+1], "type": "LN", "art": None, "law": law })

                elif paragraph.endswith(":"):
                        never = 0
                        # pprint(paragraphs[count])
                        text = paragraphs[count]
                        orgs.append({"text":text, "type": "P", "art": art, "law": law })
                
                elif count != never:
                    #  pprint(paragraph)
                     text = paragraphs[count]
                     orgs.append({"text":text, "type": "T", "art": art, "section": section, "sub_section": ssection,"cap":cap  })
                
            orgs_3 = orgs
            orgs = []     
            for item in sorted([org for org in orgs if org["type"] in ["SSN", "SN", "CN"]], key=lambda d: d['text']):
                 pprint(item['text']) 


            

            return
            value = 0
            users = ["Hamilton","Faustina"]
            # current_user =words[0]
            description = ""
            result = { 
                 users[0]: {
                 'in': 0,
                 'out': 0
            },
            users[1]:{
                 'in': 0,
                 'out': 0
            }}
            # pprint(all_data)
            all_lines = []
            cap_number = 0
            return
            for word in w:

                pprint(word)
                return
                cap_number = cap_number + 1
                seccao_number = 0
                all_lines.append(f"Capitulo {cap_number}")
                for seccao in cap.split("SECÇÃO"):
                    seccao_number = seccao_number + 1
                    all_lines.append(f"SECÇÃO {seccao_number}")

                    sub_seccao_number = 0
                    for sub_seccao in seccao.split("SUB-SECÇÃO"):
                        sub_seccao_number = sub_seccao_number + 1
                        all_lines.append(f"SUB-SECÇÃO {sub_seccao_number}")
                        # pprint(seccao)
                        for art in sub_seccao.split("Artigo "):
                            for line in art.split("\n"):
                                if str(line.split(".º")[0]).isnumeric():
                                    a = f"Artigo {str(line.split('.º')[0])}"
                                    #    pprint(a)
                                    all_lines.append(a)
                                if line != "" and not str(line.split(".º")[0]).isnumeric():
                                    a = line.replace("- ","")
                                    #    pprint(a)
                                    all_lines.append(a)

            count = -1
            new_structre = []
            art = ""
            title = ""
            line = 0
            # pprint(all_lines)

            artigo = None
            count = -1
            line = 0
            for h in all_lines:
                count = count + 1
                if "Artigo " in h:
                     line = 0
                     pprint(h)
                     pprint(f"Topico {all_lines[count+1]}")
                
                elif ":" in h:
                      pprint(f'Inicio {h.replace(":","")}')
                elif "Artigo " in all_lines[count-1]:
                      pass
                else:
                      line = line + 1
                      pprint(f'{line} - {h}')


            return

            for all_line in all_lines:
                 pprint(all_line)
                 count = count + 1
                #  pprint(count)
                 new_structre.append(None)
                 if len(all_line) < 6 or all_line=="\n":
                      break
                #  if "SECÇÃO " in all_line:
                #       section = str(all_line.split(" ")[1]).replace("\n")
                #       new_structre[count] = {"text": all_line.split(" ")[1], "type": "Section", "art": "", "section": section}
                #       break
                #  if "TÍTULO " in all_line:
                #       title = str(all_line.split(" ")[1]).replace("\n")
                #       new_structre[count] = {"text": all_line.split(" ")[1], "type": "Title", "art": "", "title": title}
                #       break
                #  if "Artigo " in all_line:
                #       art = all_line.split(" ")[1]

                #       new_structre[count] = {"text": all_line.split(" ")[1], "type": "Artigo", "art": art, "title": title}
                #       break
                 
                
                #  if ":" in all_line:
                #       line = 0
                #       new_structre[count-1] = {"text": all_line[count-1], "type": "Pos-Artigo", "art": art, "title": title}
                #       new_structre[count] = {"text": all_line.replace(":","", "Pre-linha"), "art": art, "title": title}
                #       break
                 
                #  line = line + 1
                #  new_structre[count] = {"text": all_line, "art": art, "title": title, "line": line}

                 

                #  pprint("*")
                #  pprint(all_line)

            # pprint(new_structre)


                          


               