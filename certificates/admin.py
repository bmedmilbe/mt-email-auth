from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from . import models
import json
from datetime import date
from pprint import pprint
from django.conf import settings
import os
from django.utils.text import slugify
# Register your models here.
from django.core.files import File
from openpyxl import load_workbook
from io import BytesIO
import requests
from django.core.files.storage import default_storage
from pathlib import Path
# from django.db.migrations.recorder import MigrationRecorder


# @admin.register(models.Colaborator)
# class ColaboratorAdmin(admin.ModelAdmin):
#     list_display = ["customer"]
#     search_fields = ["customer__user__first_name__istartswith"]


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user"]

    list_per_page = 10
    ordering = ["user"]


@admin.register(models.PersonBirthAddress)
class PersonBirthAddressAdmin(admin.ModelAdmin):
    list_display = ["birth_street"]


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    prepopulated_fields = {"slug": ("name",)}  # new

    list_per_page = 10
    ordering = ["name"]


@admin.register(models.County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    prepopulated_fields = {"slug": ("name",)}  # new

    list_per_page = 10
    ordering = ["name"]


@admin.register(models.Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ["name", "county"]
    prepopulated_fields = {"slug": ("name",)}  # new

    list_per_page = 10
    ordering = ["name"]


@admin.register(models.Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ["name", "town"]
    list_editable = ["town"]
    prepopulated_fields = {"slug": ("name",)}  # new
    list_per_page = 50
    ordering = ["name"]


@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["house_number", "street"]
    list_per_page = 10
    ordering = ["street", "house_number"]


@admin.register(models.IDType)
class IDTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_per_page = 10


@admin.register(models.Parent)
class ParentsAdmin(admin.ModelAdmin):

    list_display = ["title", "in_plural", "in_plural_mix", "gender", "degree"]
    list_editable = ["in_plural", "in_plural_mix", "gender", "degree"]
    ordering = ["degree"]
    list_per_page = 10


@admin.register(models.Coval)
class CovalsAdmin(admin.ModelAdmin):

    list_display = ["number", "nick_number", "date_used", "square"]
    list_editable = ["date_used", "square"]
    ordering = ["date_used"]
    list_per_page = 30

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


        # reading csv file 
        if obj.catalogue != None:
            # df = pd.read_csv(obj.catalogue.path)
            # print(df.head())
            pass
        
        if obj.cards.url != None:
            # pprint(File(open(obj.cards.url, 'rb')))
            url = obj.cards.url
            # url = "http://127.0.0.1:8000/media/camaramz/posts/documents/text_cecab_rubish_1.docx"
            docx = BytesIO(requests.get(url).content)
            # Write the stuff
            with open("output.xlsx", "wb") as f:
                f.write(docx.getbuffer())
                # pprint(docx)
                # pass
            workbook = load_workbook(filename="output.xlsx")
            sheet = workbook["Uploaded"]
            m = hashlib.sha256()
            for row in range(2, sheet.max_row+1):
                card_number = int(sheet[f"a{row}"].value)+100000
                size = len(str(card_number))
                zerros = (6-size) * "0" 
                
                venv = settings.TOPUP_KEY
                number = f"{zerros}{card_number}"
                
                var =  str(str(int(sheet[f'b{row}'].value)) + venv).encode('utf-8')
            
                code = hashlib.sha224(var).hexdigest()
                # print("number: ", number)
                # print("code: ", code)
                
                key = Fernet.generate_key()
                fernet = Fernet(key)
                # print("key: ", key)
                # encNumber = fernet.encrypt(number.encode())
                # print("encrypted number: ", encNumber)
                # decNumber = fernet.decrypt(encNumber).decode()
                # print("decrypted number: ", decNumber)
                value = str(int(sheet[f"c{row}"].value))
                # pprint(str(int(sheet[f'b{row}'].value)))



                # 1 - 3: 36 - 50 115000 - 115036 
                # 1 - 2: 24 - 100 115037 - 115060
                # 1 - 2: 24 - 200 115061 - 115084
                
                encValue = fernet.encrypt(value.encode())
                # print("encrypted value: ", encValue)
                decValue = fernet.decrypt(encValue).decode()
                # print("decrypted value: ", decValue)
                
                models.Card.objects.create(
                    number=number,
                    code =code,
                    key=key,
                    value = encValue,
                    # currency=sheet[f'c{row}'].value
                    currency_id=2

                )
            # for card in models.Card.objects.all():
            #     fernet = Fernet(card.key)
                # pprint(card.number)
                # pprint(card.code)
                # pprint(fernet.decrypt(bytes(card.value)).decode())

           




@admin.register(models.Cemiterio)
class CemiterioAdmin(admin.ModelAdmin):

    list_display = ["name", "county"]
    list_per_page = 10

    cemiterios = [
{"distrito_id":"2","distrito_name":"Trindade","distrito_active":"1"},
{"distrito_id":"3","distrito_name":"Madalena","distrito_active":"1"}
]


@admin.register(models.BiuldingType)
class BuldingTypeAdmin(admin.ModelAdmin):

    list_display = ["name", "prefix"]
    list_per_page = 10

    data = [
{"autocreatetype_id":"1","autocreatetype_name":"um edifício"},
{"autocreatetype_id":"2","autocreatetype_name":"um edifício e respectivo muro de vedação"},
{"autocreatetype_id":"3","autocreatetype_name":"muro de vedação"},
{"autocreatetype_id":"4","autocreatetype_name":"uma barraca"},
{"autocreatetype_id":"5","autocreatetype_name":"um quiosque"},
{"autocreatetype_id":"6","autocreatetype_name":"um estabelecimento comercial"}
]


@admin.register(models.CovalSalles)
class CovalSallesAdmin(admin.ModelAdmin):

    list_display = ["coval", "person"]
    list_per_page = 10


@admin.register(models.Change)
class ChangesAdmin(admin.ModelAdmin):

    list_display = ["name", "price"]
    list_editable = ["price"]
    list_per_page = 10


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        # Open and read the JSON file
        count = 1
        with open('bis.json', 'r') as file:
            data = list(json.load(file))
            for person in data:
                newperson = models.Person()
                newperson.id_type_id = int(person["bi_documento"])
                newperson.id_issue_date = f"{person['bi_emi_ano']}-{person['bi_emi_mes']}-{person['bi_emi_dia']}"
                
                try:
                    date(year=person['bi_emi_ano'],month=person['bi_emi_mes'],day=person['bi_emi_dia'])
                    newperson.id_issue_date = f"{person['bi_emi_ano']}-{person['bi_emi_mes']}-{person['bi_emi_dia']}"
                except:
                    newperson.id_issue_date = f"{person['bi_emi_ano']}-{person['bi_emi_mes']}-{27}"

                if int(person["bi_estado"]) == 1:
                    newperson.status = "S"
                elif int(person["bi_estado"]) == 2:
                    newperson.status = "M"
                elif int(person["bi_estado"]) == 3:
                    newperson.status = "L"
                elif int(person["bi_estado"]) == 4:
                    newperson.status = "V"
                elif int(person["bi_estado"]) == 5:
                    newperson.status = "D"
                elif int(person["bi_estado"]) == 6:
                    newperson.status = "D"

                # pprint(newperson.status)

                newperson.id = person["bi_id"]
                newperson.id_issue_local_id = int(person["bi_local_emi"])
                newperson.mother_name = person["bi_mae"]
                newperson.father_name = person["bi_pai"]
                newperson.name = person["bi_name"]
                newperson.birth_date = f"{person['bi_nasc_ano']}-{person['bi_nasc_mes']}-{person['bi_nasc_dia']}"
                # newperson.birth_address = None
                try:
                    date(year=int(person['bi_nasc_ano']),month=int(person['bi_nasc_mes']),day=int(person['bi_nasc_dia']))
                    newperson.birth_date = f"{person['bi_nasc_ano']}-{person['bi_nasc_mes']}-{person['bi_nasc_dia']}"

                except ValueError:
                    newperson.birth_date = f"{person['bi_nasc_ano']}-{person['bi_nasc_mes']}-{27}"

                newperson.id_number = person["bi_number"]
                newperson.gender = "F" if int(person["bi_sexo"]) == 2 else "M"
                
                # obj = models.Person.objects.filter(id=newperson.id)
                # if not obj.exists():
                #     # if newperson.status == "F":
                #         # pprint(newperson.status)
                #     # newperson.save()
                #     pass
                # else:
                #     obj = obj.first()
                #     obj.id_type_id = int(person["bi_documento"])
                #     obj.id_issue_date = f"{person['bi_emi_ano']}-{person['bi_emi_mes']}-{person['bi_emi_dia']}"
                    
                #     try:
                #         date(year=person['bi_emi_ano'],month=person['bi_emi_mes'],day=person['bi_emi_dia'])
                #         obj.id_issue_date = f"{person['bi_emi_ano']}-{person['bi_emi_mes']}-{person['bi_emi_dia']}"
                #     except:
                #         obj.id_issue_date = f"{person['bi_emi_ano']}-{person['bi_emi_mes']}-{27}"

                #     if int(person["bi_estado"]) == 1:
                #         obj.status = "S"
                #     elif int(person["bi_estado"]) == 2:
                #         obj.status = "M"
                #     elif int(person["bi_estado"]) == 3:
                #         obj.status = "L"
                #     elif int(person["bi_estado"]) == 4:
                #         obj.status = "V"
                #     elif int(person["bi_estado"]) == 5:
                #         obj.status = "D"
                #     elif int(person["bi_estado"]) == 6:
                #         obj.status = "D"

                   

                    
                #     obj.id_issue_local_id = int(person["bi_local_emi"])
                #     obj.mother_name = person["bi_mae"]
                #     obj.father_name = person["bi_pai"]
                #     obj.name = person["bi_name"]
                #     obj.birth_date = f"{person['bi_nasc_ano']}-{person['bi_nasc_mes']}-{person['bi_nasc_dia']}"
                #     # obj.birth_address = None
                #     try:
                #         date(year=int(person['bi_nasc_ano']),month=int(person['bi_nasc_mes']),day=int(person['bi_nasc_dia']))
                #         obj.birth_date = f"{person['bi_nasc_ano']}-{person['bi_nasc_mes']}-{person['bi_nasc_dia']}"

                #     except ValueError:
                #         obj.birth_date = f"{person['bi_nasc_ano']}-{person['bi_nasc_mes']}-{27}"

                #     obj.id_number = person["bi_number"]
                #     obj.gender = "F" if int(person["bi_sexo"]) == 2 else "M"
                    
                    # obj.save()
                    




        # Print the data

        # persons = models.Person.objects.all()

        # for person in persons:
            

        #     # if person.id != 521:
        #     #     person.birth_date = date(
        #     #         person.birth_year, person.birth_month, person.birth_day)
        #     #     person.id_issue_date = date(
        #     #         person.id_issue_year, person.id_issue_month, person.id_issue_day)
        #     #     # person.id_expire_date = date(
        #     #     #     person.id_expire_year, person.id_expire_month, person.id_expire_day)

        #     # if person.bi_sexo == 2:
        #     #     person.gender = "F"
        #     # elif person.bi_sexo == 1:
        #     #     person.gender = "M"

        #     # if person.bi_estado == 1:
        #     #     person.status = "S"
        #     # elif person.bi_estado == 2:
        #     #     person.status = "M"
        #     # elif person.bi_estado == 3:
        #     #     person.status = "L"
        #     # elif person.bi_estado == 4:
        #     #     person.status = "V"
        #     # elif person.bi_estado == 5:
        #     #     person.status = "D"
        #     # elif person.bi_estado == 6:
        #     #     person.status = "D"

        #     # if person.id_issue_local.id == 13:
        #     #     person.nationality_id = 3
        #     # if person.father_name == "-1":
        #     #     person.father_name = None
        #     # if person.mother_name == "-1":
        #     #     person.mother_name = None
            
        #     # pprint("passou")


        #     # person.save()
        #     pass
        return super().get_queryset(request)
    list_display = [
        "name",
        "surname",
        "gender",

        "birth_date",
        # "birth_street",
        # "birth_town" ,
        # "birth_county",
        # "birth_country" ,

        "id_type",
        "id_number",
        "id_issue_local",
        # "id_issue_country",
        "id_issue_date",
        "id_expire_date",

        "father_name",
        "mother_name",

        "address",

        "status"
    ]

    list_per_page = 10
    ordering = ["name", "surname"]
    list_filter = ["status", "gender"]


@admin.register(models.CertificateTypes)
class CertificateTypesAdmin(admin.ModelAdmin):
    list_display = [
        "name", "gender"
    ]

    prepopulated_fields = {"slug": ("name",)}  # new

    list_editable = [
        "gender"
    ]

    # def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
    #     types = models.CertificateTypes.objects.all()

    #     for certificate in types:
    #         certificate.slug = slugify(certificate.name)
    #         print(certificate.slug)
    #         certificate.save()


@admin.register(models.Instituition)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

    list_per_page = 10
    ordering = ["name"]
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        entities = [{"entidade_id":"35","entidade_name":"DEF-PRAIA"},
            {"entidade_id":"36","entidade_name":"SME-Luanda"},
            {"entidade_id":"37","entidade_name":"DEF"},
            {"entidade_id":"38","entidade_name":"DEF Secção Emissão Passaportes"},
            {"entidade_id":"39","entidade_name":"Centro de Formação Profissional AJOLFE"},
            {"entidade_id":"40","entidade_name":"Préfecture de la Haute-Savole Annecy (74000)"},
            {"entidade_id":"41","entidade_name":"Embaixada em Angola"},
            {"entidade_id":"42","entidade_name":"SR\/DPF\/SP"},
            {"entidade_id":"43","entidade_name":"DPF\/SSB\/SP"},
            {"entidade_id":"44","entidade_name":"SR\/DPF\/GO"},
            {"entidade_id":"45","entidade_name":"Serviço Nacional de Migração"},
            {"entidade_id":"46","entidade_name":"PCO,DAR ES SALAAM"},
            {"entidade_id":"47","entidade_name":"DEF Delegação da Boa Vista"},
            {"entidade_id":"48","entidade_name":"Embaixada de Cabo Verde em Lisboa"}
            ]

           


        for entity in entities:
            new_entity = models.Instituition()
            new_entity.id = entity['entidade_id']
            new_entity.name = entity['entidade_name']

            if not models.Instituition.objects.filter(id=new_entity.id).exists():
                # new_entity.save()
                pass
        return super().get_queryset(request)



@admin.register(models.Ifen)
class IfenAdmin(admin.ModelAdmin):
    list_display = [
        "name",  "size",
    ]

    list_per_page = 10
    list_editable = ["size"]


  
@admin.register(models.University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

    list_per_page = 10
    ordering = ["name"]


@admin.register(models.CertificateTitle)
class CertificateTitleAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "name", "certificate_type", "type_price", "goal"
                    ]

    list_editable = ["certificate_type", "type_price", "goal"]

    list_per_page = 100
    ordering = ["id", "certificate_type", "name"]

    prepopulated_fields = {"slug": ("name",)}  # new
    
    

    # def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
    #     title = models.CertificateTitle.objects.all()

    #     for certificate in title:
    #         certificate.slug = slugify(certificate.name)
    #         certificate.save()


@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        
        # certificates = list(models.Certificate.objects.order_by("-id"))
        # # certificates = []
        # for item in certificates:
        #     if not item.file.storage.exists(item.file.name):
        #         # file_path = item.number
        #         new_folder= f"/certificates/{item.type.id}-{item.type.certificate_type.slug}-de-{item.type.slug}"
        #         current_folder= f"/certificates/gerados3/{item.type.certificate_type.id}/{item.type.id}"
        #         file_path = f"{str(settings.MEDIA_ROOT)}{current_folder}/{item.number}.pdf"
        #         # # pprint(file_path)
        #         # original_file_path = Path(file_path)
        #         # # Create a new File object from the moved file path
        #         if os.path.exists(file_path):
        #         #     with default_storage.open(file_path, 'rb') as f:
        #         #         new_file = File(f)
        #         #         item.file = new_file
        #         #         item.save()
        #         # else:
        #         #     pprint(file_path)
        #         # # Assign the new File object to the copied_file field
        #         # self.copied_file = new_file 
        #         # if os.path.exists(file_path):
        #         #     # os.mkdir(f"{str(settings.MEDIA_ROOT)}{folder}")

        #         #     # file_path = f"{new_folder}/{item.number}.pdf"
        #             # file_path = f"{new_folder}/{item.number}.pdf"
        #             file_path_online = f"{item.type.id}-{item.type.certificate_type.slug}-de-{item.type.slug}/{item.number}.pdf"
                    
        #             try:
                        
        #                 with open(file_path, 'rb') as output:
        #                     item.file.save(f'{file_path_online}', File(output))
        #                     # file_path = item.file.url
        #                     # pprint(file_path_online)
        #                     pass

        #             except Exception as e:
        #                 print("error", e)
        #         else:
        #             # print("not founf", file_path)

        #             # pprint(file_path)
        #             pass
            
        
        # Open and read the JSON file
        # count = 1
        # with open('atestados.json', 'r') as file:
        #     data = list(json.load(file))
        #     for certificate in   sorted(data, key=lambda x: x["atestado_id"]):
        #         newcertificate = models.Certificate()
        #         newcertificate.id = int(certificate["atestado_id"])
               
        #         cer = models.Certificate.objects.filter(id=int(certificate["atestado_id"])).first()
        #         if cer != None:
        #             cer.date_issue = f"{certificate['atestado_date']}"
        #             # pprint(cer.date_issue)

        #             cer.save()
        #             # pass
                
                    
                    
                # newcertificate.date_issue = f"{certificate['atestado_date']}"


        #         newcertificate.id = int(certificate["atestado_id"])
        #         newcertificate.main_person_id = int(certificate["atestado_bi"])
        #         newcertificate.type_id = int(certificate["atestado_type"])
                
        #         newcertificate.status = certificate["atestado_state"]
        #         state = int(certificate["atestado_state"])
        #         if state == 1:
        #             newcertificate.status = "P"
        #         elif state == 2:
        #             newcertificate.status = "R"
        #         elif state == 3:
        #             newcertificate.status = "C"
        #         elif state == 4:
        #             newcertificate.status = "F"
        #         elif state == 5:
        #             newcertificate.status = "A"


        #         newcertificate.date_issue = f"{certificate['atestado_date']}"
        #         newcertificate.obs = certificate["atestado_obs"]
        #         newcertificate.number = f"{certificate['atestado_number']}"
        #         newcertificate.type_id1 = int(certificate["atestado_type1"])
                
        #         cer = models.Certificate.objects.filter(id=int(certificate["atestado_id"]))
        #         if not cer.exists():

        #             # newcertificate.save()
        #             pass
        #         else:
        #             cer = cer.first()
        #             cer.date_issue = f"{certificate['atestado_date']}"
        #             # cer.save()
                    

                    
                
        
        #             # cer.main_person_id = int(certificate["atestado_bi"])
        #             # cer.type_id = int(certificate["atestado_type"])
                    
        #             # cer.status = certificate["atestado_state"]
        #             # state = int(certificate["atestado_state"])
        #             # if state == 1:
        #             #     cer.status = "P"
        #             # elif state == 2:
        #             #     cer.status = "R"
        #             # elif state == 3:
        #             #     cer.status = "C"
        #             # elif state == 4:
        #             #     cer.status = "F"
        #             # elif state == 5:
        #             #     cer.status = "A"


        #             # cer.date_issue = f"{certificate['atestado_date']}"
        #             # cer.obs = certificate["atestado_obs"]
        #             # cer.number = f"{certificate['atestado_number']}"
        #             # cer.type_id1 = int(certificate["atestado_type1"])
        #             # cer.save()
                    


        #         # if cer.exists():
        #         #     cer = cer.first()
        #         #     cer.date_issue = f"{certificate['atestado_date']}"
        #         #     cer.save()
        #         #     # newcertificate.save()
        #         #     pprint(newcertificate)
        #         #     pass
        return super().get_queryset(request)
    
    # def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
    #     certificates = models.Certificate.objects.order_by("id")
    #     count = int(settings.MOVED)
    #     for certificate in certificates[count:]:
    #         count = count+1

    #         if certificate.atestado_state == 1:
    #             certificate.status = "P"
    #         elif certificate.atestado_state == 2:
    #             certificate.status = "R"
    #         elif certificate.atestado_state == 4:
    #             certificate.status = "F"
    #         elif certificate.atestado_state == 3:
    #             certificate.status = "C"
    #         elif certificate.atestado_state == 5:
    #             certificate.status = "A"

    #         certificate.save()

    #     # # # # pprint(certificate)
        #     if count > int(settings.MOVED):
        #         file_path = certificate.number
        #         file_path = f"/certificates/{certificate.type.certificate_type.id}/{certificate.type.id}/{certificate.number}.pdf"
        #         folder_online = f"{certificate.type.id}-{certificate.type.certificate_type.slug}-de-{certificate.type.slug}/{certificate.number}.pdf"

        #         if os.path.exists(str(settings.MEDIA_ROOT) + f"{file_path}"):
        #             with open(str(settings.MEDIA_ROOT) + f"{file_path}", 'rb') as existing_file:
                        
        #                 # pprint(certificate.type.certificate_type.slug)
        #                 certificate.file.save(f'{folder_online}', existing_file)
        #                 pprint(count)
        #         else:
        #             pprint(str(settings.MEDIA_ROOT) + f"{file_path}")

        # return super().get_queryset(request)

    list_display = [
        "type", "number", "date_issue", "main_person","secondary_person"
    ]

    list_per_page = 50
    ordering = ["-id"]
    list_filter = ["type",
                   "status"
                   ]


@admin.register(models.CertificateData)
class CertificateDataAdmin(admin.ModelAdmin):
    list_display = [
        "certificate", "house",
    ]

    list_per_page = 10
    ordering = ["-certificate__number"]


# admin.site.register(MigrationRecorder.Migration)
