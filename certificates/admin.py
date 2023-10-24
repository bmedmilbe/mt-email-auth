from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from . import models
from datetime import date
from pprint import pprint
# Register your models here.


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
        "gender",

        "birth_date",
        # "birth_street",
        # "birth_town" ,
        # "birth_county",
        # "birth_country" ,

        "id_type",

        "id_number",
        "id_issue_local",
        "id_issue_country",
        "id_issue_date",
        "id_expire_date",

        "father_name",
        "mother_name",

        "address",

        "status"]

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

    list_per_page = 10
    ordering = ["id", "certificate_type", "name"]

    prepopulated_fields = {"slug": ("name",)}  # new


@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        certificates = models.Certificate.objects.all()

        for certificate in certificates:

            if certificate.atestado_state == 1:
                certificate.status = "P"
            elif certificate.atestado_state == 2:
                certificate.status = "P"
            elif certificate.atestado_state == 4:
                certificate.status = "F"
            elif certificate.atestado_state == 3:
                certificate.status = "C"

            certificate.save()
        return super().get_queryset(request)

    list_display = [
        "type", "number", "text", "main_person", "secondary_person", "date_issue"
    ]

    list_per_page = 10
    ordering = ["-number"]
    list_filter = ["type"]


@admin.register(models.CertificateData)
class CertificateDataAdmin(admin.ModelAdmin):
    list_display = [
        "certificate", "house",
    ]

    list_per_page = 10
    ordering = ["-certificate__number"]
    # list_filter =["type"]


# @admin.register(models.Airport)
# class AirportAdmin(admin.ModelAdmin):
#     list_display = ["name", "initial", "country"]
#     prepopulated_fields = {"slug": ("name",)}  # new

#     list_per_page = 10
#     ordering = ["name"]


# @admin.register(models.FligthsCompany)
# class FligthsCompanyAdmin(admin.ModelAdmin):
#     list_display = ["name"]
#     prepopulated_fields = {"slug": ("name",)}  # new

#     list_per_page = 10
#     ordering = ["name"]


# @admin.register(models.Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = [
#         "name",
#     ]

#     search_fields = ["user__first_name__istartswith", "user__last_name__istartswith"]
#     list_per_page = 10
#     ordering = ["user__first_name"]

#     def name(self, customer: models.Customer):
#         return f"{customer.user.first_name} {customer.user.last_name}"


# @admin.register(models.Parcel)
# class ParcelAdmin(admin.ModelAdmin):
#     list_display = [
#         "customer",
#         "weigth",
#         "status",
#         "price",
#         "colaborator_get",
#         "colaborator_deliver",
#         "date_collection",
#         "address_from",
#     ]
#     # search_fields = ['post_code__istartswith', "name__istartswith",
#     #                  "customer__first_name__istartswith", "customer__last_name__istartswith"]

#     list_editable = [
#         "colaborator_get",
#         "colaborator_deliver",
#         "status",
#         "date_collection",
#     ]
#     autocomplete_fields = [
#         "customer",
#         "colaborator_get",
#         "colaborator_deliver",
#     ]
#     search_fields = [
#         "customer__user.first__name__istartswith",
#         "address_from__post_code__istartswith",
#         "created_at__istartswith",
#     ]

#     list_per_page = 30
#     ordering = ["-created_at", "customer"]
#     list_filter = [
#         "customer",
#         "colaborator_get",
#         "colaborator_deliver",
#         "date_collection",
#     ]

#     # def get_queryset(self, request: HttpRequest):
#     #     return super().get_queryset(request)


# @admin.register(models.Fligth)
# class FligthAdmin(admin.ModelAdmin):
#     list_display = [
#         "customer",
#         "weigth",
#         "status",
#         "price",
#         "payment_status",
#         "departure_at",
#         "arrive_at",
#         "arrive_to",
#         "price",
#         "number",
#         "company",
#     ]
#     search_fields = [
#         "customer__user.first__name__istartswith",
#         "departure_from.name__istartswith",
#         "arrive_to__name__istartswith",
#         "company__name__istartswith",
#     ]

#     list_editable = ["status"]
#     autocomplete_fields = [
#         "customer",
#     ]

#     list_per_page = 30
#     ordering = ["-created_at", "customer"]
#     list_filter = [
#         "customer",
#         "departure_from",
#         "arrive_to",
#         "company",
#     ]

#     search_fields = [
#         "post_code__istartswith",
#         "name__istartswith",
#         "customer__first_name__istartswith",
#         "customer__last_name__istartswith",
#     ]

#     # def get_queryset(self, request: HttpRequest):
#     #     return super().get_queryset(request)


# @admin.register(models.ShippimentFligth)
# class ShippimentFligthAdmin(admin.ModelAdmin):
#     list_display = [
#         "parcel",
#         "fligth",
#         "colaborator_from",
#         "colaborator_to",
#     ]

#     list_editable = ["colaborator_from", "colaborator_to"]

#     list_per_page = 30
#     ordering = ["-created_at"]
#     list_filter = [
#         "colaborator_from",
#         "colaborator_to",
#         "created_at",
#     ]
