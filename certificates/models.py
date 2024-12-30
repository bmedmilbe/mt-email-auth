from django.conf import settings
from django.db import models
from uuid import uuid4
from pprint import pprint
from django.core.validators import MinValueValidator
from datetime import datetime


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    level = models.IntegerField(default=1, null=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"


class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    code = models.IntegerField(null=True)
    # stp

    def __str__(self) -> str:
        return f"{self.name}"


class Parent(models.Model):
    title = models.CharField(max_length=255)
    in_plural = models.CharField(max_length=255)
    in_plural_mix = models.CharField(max_length=255)
    degree = models.IntegerField(default=1)

    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    ]
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default="M"
    )

    def __str__(self) -> str:
        return f"{self.title}"


class County(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # mezochi

    def __str__(self) -> str:
        return f"{self.name} - {self.country.name}"


class Town(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True)
    # trindade/madelena#bombom

    def __str__(self) -> str:
        return f"{self.name} - {self.county.name}"


class Cemiterio(models.Model):
    name = models.CharField(max_length=255)

    county = models.ForeignKey(County, on_delete=models.CASCADE)

    # stp
    def __str__(self) -> str:
        return f"{self.name}"


class Coval(models.Model):
    nick_number = models.CharField(max_length=255)
    number = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    date_used = models.DateField()
    date_of_deth = models.DateField(null=True, blank=True)
    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    ]
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=GENDER_MALE
    )
    SQUARE_A = "A"
    SQUARE_B = "B"
    SQUARE_C = "C"
    SQUARE_D = "D"
    SQUARE_CHOICES = [
        (SQUARE_A, "A"),
        (SQUARE_B, "B"),
        (SQUARE_C, "C"),
        (SQUARE_D, "D"),
    ]
    square = models.CharField(
        max_length=1, choices=SQUARE_CHOICES, default=SQUARE_A
    )
    closed = models.BooleanField(default=False)
    selled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.number}{self.square} | {self.nick_number}"

    cemiterio = models.ForeignKey(
        Cemiterio, on_delete=models.PROTECT, default=1)


class Change(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class BiuldingType(models.Model):
    name = models.CharField(max_length=255)
    prefix = models.CharField(
        max_length=255, default="", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.prefix} {self.name}"


class Street(models.Model):
    name = models.CharField(max_length=255)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=255)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True)
    # piedade

    def __str__(self) -> str:
        return f""
        return f"{self.name} - {self.town.name}"


class House(models.Model):
    house_number = models.CharField(max_length=255, null=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)

    # 123, nao tem

    def __str__(self) -> str:
        return f""
        return f"{self.house_number} {self.street.name}, {self.street.town.name}, {self.street.town.county.country.name}"


class IDType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"


class PersonBirthAddress(models.Model):
    birth_street = models.ForeignKey(
        Street, on_delete=models.PROTECT, null=True, related_name="birth_person_address")
    birth_town = models.ForeignKey(
        Town, on_delete=models.PROTECT, null=True, related_name="birth_person_address")
    birth_county = models.ForeignKey(
        County, on_delete=models.PROTECT, null=True, related_name="birth_person_address")
    birth_country = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name="birth_person_address")

    def __str__(self) -> str:
        address = ""
        if self.birth_street:
            address = f"{self.birth_street.name}, "
        if self.birth_town:
            address = f"{address}{self.birth_town.name}, "
        if self.birth_county:
            address = f"distrito de {self.birth_county.name}, " if address == "" else f"{address} distrito de {self.birth_county.name}, "

        address = f"{address}{self.birth_country.name}"

        return f"{address}"


class Instituition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"


class Person(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, default="", null=True)
    birth_date = models.DateField(
        null=True, blank=True)
    birth_day = models.IntegerField(null=True)
    birth_month = models.IntegerField(null=True)
    birth_year = models.IntegerField(null=True)


    bi_nasc_loc = models.IntegerField(null=True)
    birth_address = models.ForeignKey(
        PersonBirthAddress, on_delete=models.CASCADE, related_name="persons", null=True)

    id_type = models.ForeignKey(IDType, on_delete=models.PROTECT)

    id_number = models.CharField(max_length=255)
    id_issue_local = models.ForeignKey(
        Instituition, on_delete=models.PROTECT, related_name="id_issue_person")
    id_issue_country = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name="id_issue_person", null=True)
    
    id_issue_date = models.DateField(null=True)
    id_issue_day = models.IntegerField(null=True, default=1)
    id_issue_month = models.IntegerField(null=True, default=1)
    id_issue_year = models.IntegerField(null=True, default=1)

    id_expire_date = models.DateField(null=True)
    nationality = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name="person_nationality", null=True)

    father_name = models.CharField(max_length=255, null=True)
    mother_name = models.CharField(max_length=255, null=True)

    address = models.ForeignKey(
        House, on_delete=models.PROTECT, related_name='person', null=True)

    MARRITIAL_STATUS_MARRIED = "M"
    MARRITIAL_STATUS_SINGLE = "S"
    MARRITIAL_STATUS_LIVING_TOGETHER = "L"
    MARRITIAL_STATUS_VIUVO = "V"
    MARRITIAL_STATUS_DIVOCIED = "D"
    MARRITIAL_STATUS_CHOICES = [
        (MARRITIAL_STATUS_MARRIED, "Married"),
        (MARRITIAL_STATUS_SINGLE, "Single"),
        (MARRITIAL_STATUS_LIVING_TOGETHER, "Living together"),
        (MARRITIAL_STATUS_VIUVO, "Viuvo"),
        (MARRITIAL_STATUS_DIVOCIED, "Divorcied"),
    ]

    bi_estado = models.IntegerField(null=True)
    bi_sexo = models.IntegerField(null=True)

    status = models.CharField(
        max_length=1, choices=MARRITIAL_STATUS_CHOICES, null=True
    )

    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    ]
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True
    )

    def __str__(self) -> str:
        return f"{self.name} {self.surname} with {self.id_type.name} {self.id_number} from {self.nationality.name if self.nationality != None else '' }"


class CertificateTypes(models.Model):
    name = models.CharField(max_length=255)
    GENDER_MALE = "o"
    GENDER_FEMALE = "a"
    GENDER_CHOICES = [
        (GENDER_MALE, "o"),
        (GENDER_FEMALE, "a"),
    ]
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=GENDER_MALE, null=True
    )
    slug = models.SlugField(max_length=255, null=True)
    # atestado
    # certidao
    # autorizacao
    # licenca

    def __str__(self) -> str:
        return f"{self.name}"


class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"


class Ifen(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField()

    def __str__(self) -> str:
        return str(self.size)


class CertificateTitle(models.Model):

    name = models.CharField(max_length=255)  # residencia
    certificate_type = models.ForeignKey(
        CertificateTypes, on_delete=models.CASCADE, null=True)
    type_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True)
    goal = models.CharField(max_length=255, null=True)  # de/para fins de/
    # atestado de residencia
    slug = models.SlugField(max_length=255, null=True)

    def __str__(self) -> str:
        return f"{self.certificate_type.name} {self.goal} {self.name}"


class Certificate(models.Model):

    
    id = models.AutoField(primary_key=True)

    type = models.ForeignKey(
        CertificateTitle, on_delete=models.PROTECT, null=True)
    number = models.CharField(max_length=255, null=True)
    date_issue = models.DateTimeField(auto_now=True, null=True)
    text = models.TextField(default="", null=True)
    main_person = models.ForeignKey(
        Person, on_delete=models.PROTECT, related_name="main_person_certificates", null=True)
    secondary_person = models.ForeignKey(
        Person, on_delete=models.PROTECT, null=True, related_name="second_person_certificates")
    house = models.ForeignKey(
        House, on_delete=models.PROTECT, related_name="certificates", null=True)
    file = models.FileField(
        upload_to='camaramz/certificates', null=True, blank=True)

    STATUS_COMPLETED = "C"
    STATUS_FAILD = "F"
    STATUS_PENDENT = "P"
    STATUS_REVIEWED = "R"
    STATUS_ARCHIVED = "A"
    STATUS_CHOICES = [
        (STATUS_COMPLETED, "Concluído"),
        (STATUS_FAILD, "Incorrecto"),
        (STATUS_PENDENT, "Pendente"),
        (STATUS_REVIEWED, "Revisto"),
        (STATUS_ARCHIVED, "Archived"),
    ]

    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=STATUS_PENDENT, null=True
    )

    obs = models.TextField(null=True)

    atestado_state = models.IntegerField(null=True, default=1)
    type_id1 = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.type.name} {self.number}"


class CertificateSimplePerson(models.Model):

    type = models.ForeignKey(CertificateTitle, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Femal"),
    ]
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES
    )
    birth_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name}"

    # - Add field status to certificate
    # - Add field birth_address to person
    # - Add field birth_date to person
    # - Add field gender to person
    # - Add field id_expire_date to person
    # - Add field id_issue_country to person
    # - Add field id_issue_date to person
    # - Add field nationality to person
    # - Add field status to person


class CertificateSimpleParent(models.Model):

    type = models.ForeignKey(CertificateTitle, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    ]

    birth_date = models.DateField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class CertificateSinglePerson(models.Model):

    type = models.ForeignKey(CertificateTitle, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    ]
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES
    )

    def __str__(self) -> str:
        return f"{self.name}"


class CertificateDate(models.Model):

    type = models.ForeignKey(CertificateTitle, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()


class CertificateData(models.Model):

    # save the certificate details

    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.certificate}"


class CovalSalles(models.Model):
    coval = models.ForeignKey(Coval, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)


# class Airport(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.PROTECT)
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255)
#     initial = models.CharField(max_length=255)

#     def __str__(self) -> str:
#         return f"{self.name}"


# class CustomerAddress(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.PROTECT)
#     house_number = models.CharField(max_length=255, null=True)
#     street = models.CharField(max_length=255)
#     post_code = models.CharField(max_length=255)
#     # house_number = models.CharField(max_length=255)

#     customer = models.ForeignKey(
#         Customer, on_delete=models.PROTECT, related_name="address"
#     )

#     def __str__(self) -> str:
#         return f"{self.street}, {self.post_code}"


# class FligthsCompany(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255)

#     def __str__(self) -> str:
#         return f"{self.name}"


# class Colaborator(models.Model):
#     customer = models.OneToOneField(
#         Customer, on_delete=models.PROTECT, related_name="colaborators"
#     )

#     def __str__(self) -> str:
#         return f"{self.customer.user.first_name} {self.customer.user.last_name}"


# class Receiver(models.Model):
#     customer = models.ForeignKey(
#         Customer, on_delete=models.PROTECT, related_name="receiver"
#     )
#     name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     country = models.ForeignKey(
#         Country, on_delete=models.PROTECT, related_name="receivers"
#     )
#     house_number = models.CharField(max_length=255, null=True, blank=True, default="")
#     street = models.CharField(max_length=255)
#     post_code = models.CharField(max_length=255, null=True, blank=True, default="")

#     def __str__(self) -> str:
#         return f"{self.name} {self.country.name} {self.phone}"


# class Weigth(models.Model):
#     quantity = models.DecimalField(max_digits=4, decimal_places=2)
#     price = models.DecimalField(max_digits=4, decimal_places=2)

#     def __str__(self) -> str:
#         return f"{self.quantity} KGS"


# class Parcel(models.Model):
#     STATUS_COLLECTED = "C"
#     STATUS_SHIPPING = "M"
#     STATUS_PENDENT = "P"
#     STATUS_DELIVERED = "D"
#     STATUS_CHOICES = [
#         (STATUS_COLLECTED, "Collected"),
#         (STATUS_SHIPPING, "Shipping"),
#         (STATUS_PENDENT, "Pendent"),
#         (STATUS_DELIVERED, "Delivered"),
#     ]

#     customer = models.ForeignKey(
#         Customer, on_delete=models.PROTECT, related_name="parcels"
#     )

#     weigth = models.ForeignKey(Weigth, on_delete=models.PROTECT, related_name="parcels")
#     status = models.CharField(
#         max_length=1, default=STATUS_PENDENT, choices=STATUS_CHOICES
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     colaborator_get = models.ForeignKey(
#         Colaborator,
#         on_delete=models.PROTECT,
#         null=True,
#         related_name="colaborator_get",
#         blank=True,
#     )
#     date_collection = models.DateTimeField(null=True)
#     receiver = models.ForeignKey(
#         Receiver, on_delete=models.PROTECT, related_name="parcels"
#     )
#     address_from = models.ForeignKey(CustomerAddress, on_delete=models.PROTECT)
#     colaborator_deliver = models.ForeignKey(
#         Colaborator,
#         on_delete=models.PROTECT,
#         null=True,
#         related_name="colaborator_deliver",
#         blank=True,
#     )

#     def __str__(self) -> str:
#         return f"{self.customer.user.first_name}  {self.address_from.post_code} {self.created_at}"


# class Fligth(models.Model):
#     STATUS_ARRIVED = "A"
#     STATUS_CANCELLED = "C"
#     STATUS_PENDENT = "P"
#     STATUS_MISSID = "M"
#     STATUS_CHOICES = [
#         (STATUS_CANCELLED, "Cancelled"),
#         (STATUS_PENDENT, "Pendent"),
#         (STATUS_MISSID, "Delivered"),
#         (STATUS_ARRIVED, "Arrived"),
#     ]

#     PAYMENT_STATUS_COMPLETED = "C"
#     PAYMENT_STATUS_PENDENT = "P"
#     PAYMENT_STATUS_MISSID = "M"
#     PAYMENT_STATUS_CHOICES = [
#         (PAYMENT_STATUS_COMPLETED, "Completed"),
#         (PAYMENT_STATUS_PENDENT, "Pendent"),
#         (PAYMENT_STATUS_MISSID, "Delivered"),
#     ]

#     customer = models.ForeignKey(
#         Customer, on_delete=models.PROTECT, related_name="fligths"
#     )

#     weigth = models.ForeignKey(Weigth, on_delete=models.PROTECT, related_name="fligths")
#     status = models.CharField(
#         max_length=1, default=STATUS_PENDENT, choices=STATUS_CHOICES
#     )

#     payment_status = models.CharField(
#         max_length=1, default=PAYMENT_STATUS_PENDENT, choices=PAYMENT_STATUS_CHOICES
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     departure_at = models.DateTimeField()
#     arrive_at = models.DateTimeField()
#     departure_from = models.ForeignKey(
#         Airport, on_delete=models.PROTECT, related_name="fligths_from"
#     )
#     arrive_to = models.ForeignKey(
#         Airport, on_delete=models.PROTECT, related_name="fligths_to"
#     )
#     number = models.CharField(max_length=255)
#     company = models.ForeignKey(FligthsCompany, on_delete=models.PROTECT)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     def __str__(self) -> str:
#         return f"{self.customer.user.first_name} from {self.departure_from.name} to {self.arrive_to.name} by {self.company.name}"


# class ShippimentFligth(models.Model):
#     parcel = models.OneToOneField(
#         Parcel, on_delete=models.PROTECT, related_name="shippiment_fligths"
#     )
#     fligth = models.ForeignKey(
#         Fligth, on_delete=models.PROTECT, related_name="shippiment_fligths"
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     colaborator_from = models.ForeignKey(
#         Colaborator,
#         on_delete=models.PROTECT,
#         related_name="shippiment_from",
#         blank=True,
#     )
#     colaborator_to = models.ForeignKey(
#         Colaborator,
#         on_delete=models.PROTECT,
#         null=True,
#         related_name="shippiment_to",
#         blank=True,
#     )


# class Cart(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4)
#     weigth = models.ForeignKey(Weigth, on_delete=models.CASCADE)
#     country_from = models.ForeignKey(
#         Country, on_delete=models.CASCADE, related_name="cart_country_from"
#     )
#     country_to = models.ForeignKey(
#         Country, on_delete=models.CASCADE, related_name="cart_country_to"
#     )


# class AddressFrom(models.Model):
#     cart = models.OneToOneField(
#         Cart, on_delete=models.CASCADE, related_name="address_from"
#     )
#     house_number = models.CharField(max_length=255, null=True)
#     street = models.CharField(max_length=255)
#     post_code = models.CharField(max_length=255)


# class AddressTo(models.Model):
#     cart = models.OneToOneField(
#         Cart, on_delete=models.CASCADE, related_name="address_to"
#     )
#     receiver_name = models.CharField(max_length=255)
#     receiver_phone = models.CharField(max_length=255)
#     house_number = models.CharField(max_length=255, null=True)
#     street = models.CharField(max_length=255)
#     post_code = models.CharField(max_length=255)
# 

class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    sent = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"
