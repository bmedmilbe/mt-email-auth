from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from . import models
from datetime import date
from pprint import pprint
from django.conf import settings
import os
from django.utils.text import slugify
# Register your models here.
from django.core.files import File
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


@admin.register(models.Cemiterio)
class CemiterioAdmin(admin.ModelAdmin):

    list_display = ["name", "county"]
    list_per_page = 10


@admin.register(models.BiuldingType)
class BuldingTypeAdmin(admin.ModelAdmin):

    list_display = ["name", "prefix"]
    list_per_page = 10


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
        persons = models.Person.objects.all()

        for person in persons:

            if person.id != 521:
                person.birth_date = date(
                    person.birth_year, person.birth_month, person.birth_day)
                person.id_issue_date = date(
                    person.id_issue_year, person.id_issue_month, person.id_issue_day)
                # person.id_expire_date = date(
                #     person.id_expire_year, person.id_expire_month, person.id_expire_day)

            if person.bi_sexo == 2:
                person.gender = "F"
            elif person.bi_sexo == 1:
                person.gender = "M"

            if person.bi_estado == 1:
                person.status = "S"
            elif person.bi_estado == 2:
                person.status = "M"
            elif person.bi_estado == 3:
                person.status = "L"
            elif person.bi_estado == 4:
                person.status = "V"
            elif person.bi_estado == 5:
                person.status = "D"
            elif person.bi_estado == 6:
                person.status = "D"

            if person.id_issue_local.id == 13:
                person.nationality_id = 3

            person.save()
        return super().get_queryset(request)
    list_display = [
        "name",
        "surname",
        # "gender",

        # "birth_date",
        # "birth_street",
        # "birth_town" ,
        # "birth_county",
        # "birth_country" ,

        "id_type",

        "id_number",
        "id_issue_local",
        # "id_issue_country",
        # "id_issue_date",
        # "id_expire_date",

        "father_name",
        "mother_name",

        "address",

        # "status"
    ]

    list_per_page = 10
    ordering = ["name", "surname"]


@admin.register(models.CertificateTypes)
class CertificateTypesAdmin(admin.ModelAdmin):
    list_display = [
        "name", "gender"
    ]

    prepopulated_fields = {"slug": ("name",)}  # new

    list_editable = [
        "gender"
    ]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        types = models.CertificateTypes.objects.all()

        for certificate in types:
            certificate.slug = slugify(certificate.name)
            print(certificate.slug)
            certificate.save()


@admin.register(models.Instituition)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

    list_per_page = 10
    ordering = ["name"]


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

    #     # for certificate in title:
    #     #     # certificate.slug = slugify(certificate.name)
    #     #     certificate.save()


@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    # def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
    #     certificates = models.Certificate.objects.order_by("id")

    #     for certificate in certificates:

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
    #     # # file_path = certificate.number
    #     #     file_path = f"/certificates/{certificate.type.certificate_type.id}/{certificate.type.id}/{certificate.number}.pdf"
    #     #     folder_online = f"{certificate.type.id}-{certificate.type.certificate_type.slug}-de-{certificate.type.slug}/{certificate.number}.pdf"

    #     #     if os.path.exists(str(settings.MEDIA_ROOT) + f"{file_path}"):
    #     #         with open(str(settings.MEDIA_ROOT) + f"{file_path}", 'rb') as existing_file:
    #     #             pprint(certificate.id)
    #     #             # pprint(certificate.type.certificate_type.slug)
    #     #             # certificate.file.save(f'{folder_online}', existing_file)
    #     #     else:
    #     #         pprint(str(settings.MEDIA_ROOT) + f"{file_path}")

    #     return super().get_queryset(request)

    list_display = [
        "type", "number", "text", "main_person", "secondary_person", "date_issue"
    ]

    list_per_page = 100
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
