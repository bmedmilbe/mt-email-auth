# Create your views here.

# from msilib.schema import File
from certificates.permission import IsStaff
import stripe

import os
from io import BytesIO
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from django.db.models import Q
from django.shortcuts import render

import certificates
from certificates.serializers import BiuldingTypeSerializer, CemiterioSerializer, CertificateCommentSerializer, CertificateDateSerializer, CertificateModelAutoConstrucaoCreateSerializer, CertificateModelAutoConstrucaoSerializer, CertificateModelAutoModCovalCreateSerializer, CertificateModelAutoModCovalSerializer, CertificateModelCertCompraCovalCreateSerializer, CertificateModelCertCompraCovalSerializer, CertificateModelEnterroCreateSerializer, CertificateModelEnterroSerializer, CertificateModelFifthCreateSerializer, CertificateModelFifthSerializer, CertificateModelLicBarracaCreateSerializer, CertificateModelLicBarracaSerializer, CertificateModelLicencaBuffetCreateSerializer, CertificateModelLicencaBuffetSerializer, CertificateModelOneCreateSerializer, CertificateModelOneSerializer, CertificateModelSeventhCreateSerializer, CertificateModelSeventhSerializer, CertificateModelThreeCreateSerializer, CertificateModelThreeSerializer, CertificateModelTwoCreateSerializer, CertificateModelTwoSerializer, CertificateSerializer, CertificateSimpleParentSerializer, CertificateSimplePersonReadOnlySerializer, CertificateSimplePersonSerializer, CertificateSinglePersonSerializer, CertificateTitleSerializer, CertificateUpdateSerializer, ChangeSerializer, CountryCreateSerializer, CountrySerializer, CountyCreateSerializer, CountySerializer, CovalSerializer, CovalSetUpSerializer, CustomerSerializer, HouseCreateSerializer, HouseSerializer, IDTypeSerializer, IfenSerializer, IfenUpdateSerializer, InstituitionCreateSerializer, InstituitionSerializer, ParentSerializer, PersonBirthAddressCreateSerializer, PersonBirthAddressSerializer, PersonCreateOrUpdateSerializer, PersonSerializer, StreetCreateSerializer, StreetSerializer, TownCreateSerializer, TownSerializer, UniversityCreateSerializer, UniversitySerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import status, filters, mixins, serializers
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from pprint import pprint
from uuid import uuid4
from decimal import Decimal
# from poster.serializers import (
#     AddressFromSavedSerializer,
#     AddressFromSerializer,
#     AddressToSavedSerializer,
#     AddressToSerializer,
#     AirportSerializer,
#     CartCreateSerializer,
#     CartSerializer,
#     CountrySerializer,
#     CustomerAddressCreateSerializer,
#     CustomerAddressSerializer,
#     CustomerSerializer,
#     CustomerUpdateSerializer,
#     FligthCreateSerializer,
#     FligthSerializer,
#     FligthUpdateSerializer,
#     FligthsCompanySerializer,
#     MessagesSerializer,
#     ParcelCreateSerializer,
#     ParcelSerializer,
#     ReceiverCreateSerializer,
#     ReceiverSerializer,
#     ShippimentFligthCreateSerializer,
#     ShippimentFligthSerializer,
#     ShippimentFligthUpdateSerializer,
#     WeigthSerializer,
# )

from .models import (

    BiuldingType,
    Cemiterio,
    CertificateDate,
    CertificateSimpleParent,
    CertificateSimplePerson,
    CertificateSinglePerson,
    CertificateTitle,
    CertificateTypes,
    Change,
    Country,
    County,
    Coval,
    Customer,
    House,
    IDType,
    Ifen,
    Instituition,

    Messages,



    Certificate,
    Parent,
    Person,
    PersonBirthAddress,
    Street,
    Town,
    University
)

from .helpers import get_customer


class Pagination300(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 5000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CountrysViewSet(ModelViewSet):
    queryset = Country.objects.all().order_by("name")

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CountryCreateSerializer
        return CountrySerializer
    pagination_class = Pagination300
    permission_classes = [IsAuthenticatedOrReadOnly]


class CovalsViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Coval.objects.all().order_by("number")

    serializer_class = CovalSerializer
    pagination_class = Pagination300


class CemiteriosViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Cemiterio.objects.all().order_by("name")

    serializer_class = CemiterioSerializer
    pagination_class = Pagination300


class ChangesViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Change.objects.all()

    serializer_class = ChangeSerializer
    pagination_class = Pagination300


class UniversitysViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    queryset = University.objects.all().order_by("name")

    def get_queryset(self):
        return (University.objects.all().order_by("name"))

    
    
    def get_serializer_class(self):
        if self.request.method  in ["POST", "PUT", "PATCH"]:
            return UniversityCreateSerializer
        return UniversitySerializer
    pagination_class = Pagination300
    permission_classes = [IsAuthenticatedOrReadOnly]



class IdTypeViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericViewSet):
    queryset = IDType.objects.all().order_by("name")
    serializer_class = IDTypeSerializer
    pagination_class = Pagination300


class BiuldingTypeViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          GenericViewSet):
    queryset = BiuldingType.objects.all().order_by("name")
    serializer_class = BiuldingTypeSerializer
    pagination_class = Pagination300


class StreetsViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method in ["POST","PUT", "PATCH"]:
            return StreetCreateSerializer
        return StreetSerializer
    def get_queryset(self):
        return Street.objects.all().order_by("name")

    pagination_class = Pagination300
    permission_classes = [IsAuthenticatedOrReadOnly]
class IfenViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return IfenUpdateSerializer
        return IfenSerializer
    def get_queryset(self):
        return Ifen.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]



class InstituitionsViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.request.method in ["POST","PUT", "PATCH"]:
            return InstituitionCreateSerializer
        return InstituitionSerializer
    
    def get_queryset(self):
        return Instituition.objects.all().order_by("name")

    pagination_class = Pagination300
    permission_classes = [IsAuthenticatedOrReadOnly]



class CustomerViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        return Customer.objects.filter(user_id=self.request.user)

    def get_serializer_class(self):
        return CustomerSerializer

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = get_customer(request.user)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


class CovalSetUpViewSet(ModelViewSet):

#     permission_classes = [IsAuthenticatedOrReadOnly]


    queryset = Coval.objects.all().order_by("square", "-number")
    permission_classes = [IsStaff]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CovalSerializer
        return CovalSetUpSerializer
    pagination_class = Pagination300


class CertificateViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):

#     permission_classes = [IsAuthenticatedOrReadOnly]


    # paginator = PageNumberPagination()
    queryset = Certificate.objects.select_related(
        "type", "main_person", "house", "secondary_person").order_by("-id").all()
    pagination_class = PageNumberPagination
    permission_classes = [IsStaff]

    def get_serializer_class(self):
        if self.request.method == "PUT" or self.request.method == "PATCH":

            return CertificateUpdateSerializer
        elif self.request.method == "DELETE":

            return CertificateUpdateSerializer
        return CertificateSerializer

    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['main_person__name', 'main_person__surname', 'number__startswith',
                     "main_person__id_number", "main_person__birth_date"]
    # filterset_fields = ["status", "type__certificate_type"]

    filterset_fields = {
        'status': ['exact'],
        'type__certificate_type': ['exact', 'gt', 'lte'],
    }

    ordering_fields = ['number', "main_person__name",
                       "main_person__id_number", "main_person__birth_date", "date_issue"]


class CertificateCommentViewSet(mixins.UpdateModelMixin,  GenericViewSet):

    queryset = Certificate.objects.all()

    def get_serializer_class(self):
        return CertificateCommentSerializer


class CertificateTitleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):

#     permission_classes = [IsAuthenticatedOrReadOnly]


    queryset = CertificateTitle.objects.order_by("name").all()

    def get_serializer_class(self):
        return CertificateTitleSerializer

    filter_backends = [
                       DjangoFilterBackend]

    filterset_fields = {
        'certificate_type': ['exact', 'gt', 'lt'],
    }
    pagination_class = Pagination300



class CertificateModelViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        # return Certificate.objects.filter(type_id=self.kwargs.get('title_pk')).all()
        return Certificate.objects.all()

    def get_serializer_class(self):
        # pprint(self.kwargs)
        # return CertificateModelOneSerializer
        type_id = int(self.kwargs.get('title_pk'))
        # pprint(self.request.method)
        if self.request.method in ["POST", "PUT",  "PATCH"]:
            if type_id in [ 1, 5, 6, 7, 9, 10, 11, 15, 16, 17,
                            19, 20 , 21 , 22 , 30, 34, 68, 35]:
                # pprint(type_id)

                return CertificateModelOneCreateSerializer

            elif type_id == 2 or type_id == 4 or type_id == 8:
                # pprint(self.request.method)
                # pprint(type_id)
                return CertificateModelThreeCreateSerializer
            elif type_id == 3 or type_id == 13:
                # pprint(self.request.method)
                # pprint(type_id)
                return CertificateModelTwoCreateSerializer
            elif type_id == 12:
                # pprint(self.request.method)
                # pprint(type_id)
                return CertificateModelFifthCreateSerializer
            elif type_id == 18:
                # pprint(self.request.method)
                # pprint(type_id)
                return CertificateModelSeventhCreateSerializer
            elif type_id == 23 or type_id == 28:
                return CertificateModelAutoConstrucaoCreateSerializer
            elif type_id == 29 or type_id == 32:
                return CertificateModelLicencaBuffetCreateSerializer
            elif type_id == 24:
                return CertificateModelCertCompraCovalCreateSerializer
            elif type_id == 25:
                return CertificateModelAutoModCovalCreateSerializer
            elif type_id == 26:
                return "Registo do enterramento de cadável"
            elif type_id == 27:
                return CertificateModelLicBarracaCreateSerializer
            elif type_id == 31:
                return "Licenças Para Transladação"
            elif type_id == 33:
                # pprint(self.request.method)
                # pprint(type_id)
                return CertificateModelEnterroCreateSerializer

        if type_id == 2:
            return CertificateModelThreeSerializer
        elif type_id == 3 or type_id == 13:
            return CertificateModelTwoSerializer
        elif type_id == 12:
            return CertificateModelFifthSerializer
        elif type_id == 18:
            return CertificateModelSeventhSerializer
        elif type_id == 23 or type_id == 28:
            return CertificateModelAutoConstrucaoSerializer
        elif type_id == 24 or type_id == 30:
            return CertificateModelCertCompraCovalSerializer
        elif type_id == 25:
            return CertificateModelAutoModCovalSerializer
        elif type_id == 27:
            return CertificateModelLicBarracaSerializer
        elif type_id == 29 or type_id == 31:
            return CertificateModelLicencaBuffetSerializer
        elif type_id == 32:
            # pprint(self.request.method)
            # pprint(type_id)
            return CertificateModelEnterroSerializer
        # pprint(type_id)
        return CertificateModelOneSerializer

    def get_serializer_context(self):
        return {
            "type_id": self.kwargs.get('title_pk'),
            # "user_id": self.request.user.id
        }


class CertificatePersonsViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        type_id = int(self.kwargs.get('title_pk'))
        if type_id == 12:
            return CertificateSimplePerson.objects.filter(type_id=type_id)
        return CertificateSimplePerson.objects.filter(type_id=-1)

    def get_serializer_class(self):
        # pprint(self.kwargs)
        # return CertificateModelOneSerializer
        if self.request.method == "GET":
            return CertificateSimplePersonReadOnlySerializer
        type_id = int(self.kwargs.get('title_pk'))

        if type_id == 12:
            return CertificateSimplePersonSerializer

        # pprint(type_id)
        return CertificateSimplePersonSerializer

    def get_serializer_context(self):
        return {
            "type_id": self.kwargs.get('title_pk'),
            # "user_id": self.request.user.id
        }


class CertificateSimpleParentsViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        type_id = int(self.kwargs.get('title_pk'))
        return CertificateSimpleParent.objects.filter(type_id=type_id)

    def get_serializer_class(self):

        return CertificateSimpleParentSerializer

    def get_serializer_context(self):
        return {
            "type_id": self.kwargs.get('title_pk'),
            # "user_id": self.request.user.id
        }


class ParentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        return Parent.objects.all().order_by("id")

    def get_serializer_class(self):

        return ParentSerializer


class CertificateSinglePersonsViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        type_id = int(self.kwargs.get('title_pk'))
        if type_id == 12:
            return CertificateSinglePerson.objects.filter(type_id=type_id).all()
        return CertificateSinglePerson.objects.filter(type_id=-1)

    def get_serializer_class(self):
        # pprint(self.kwargs)
        # return CertificateModelOneSerializer
        type_id = int(self.kwargs.get('title_pk'))

        if type_id == 12:
            return CertificateSinglePersonSerializer

        # pprint(type_id)
        return CertificateSinglePersonSerializer

    def get_serializer_context(self):
        return {
            "type_id": self.kwargs.get('title_pk'),
            # "user_id": self.request.user.id
        }


class CertificateDatesViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        type_id = int(self.kwargs.get('title_pk'))
        return CertificateDate.objects.filter(type_id=type_id).all()

    def get_serializer_class(self):

        return CertificateDateSerializer

    def get_serializer_context(self):
        return {
            "type_id": self.kwargs.get('title_pk'),
            # "user_id": self.request.user.id
        }


class CertificateModelTwoViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    queryset = Certificate.objects.all()

    def get_queryset(self):
        return (
            Certificate.objects
            .filter(type_id=self.kwargs.get('title_pk'))
            .all()
        )

    def get_serializer_class(self):
        if self.kwargs.get('title_pk') == 1:
            if self.request.method == "POST":
                return CertificateModelOneCreateSerializer
            return CertificateModelOneSerializer
        elif self.kwargs.get('title_pk') == 2:
            if self.request.method == "POST":
                return CertificateModelTwoCreateSerializer
            return CertificateModelTwoSerializer

    def get_serializer_context(self):
        return {"type_id": self.kwargs.get('title_pk')}


class PersonBirthAddressViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    queryset = PersonBirthAddress.objects.all()

    def get_queryset(self):
        return (PersonBirthAddress.objects.all())

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PersonBirthAddressCreateSerializer
        return PersonBirthAddressSerializer

# class PersonBirthAddressViewSet(ModelViewSet):
  #     permission_classes = [IsAuthenticatedOrReadOnly]


#     queryset = PersonBirthAddress.objects.all()

#     def get_queryset(self):
#         return (PersonBirthAddress.objects.all())


#     def get_serializer_class(self):
#         if self.request.method == "POST":
#             return PersonBirthAddressCreateSerializer
#         return PersonBirthAddressSerializer

class CountysViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    queryset = County.objects.all().order_by("name")

    def get_queryset(self):
        return (County.objects.all().order_by("name"))

    
    
    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CountyCreateSerializer
        return CountySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    pagination_class = Pagination300





class TownViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    queryset = Town.objects.all().order_by("name")

    def get_queryset(self):
        return (Town.objects.all().order_by("name"))

    

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return TownCreateSerializer
        return TownSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = Pagination300




class HouseViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]


    queryset = House.objects.all().order_by("street__name", "house_number")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return HouseCreateSerializer
        return HouseSerializer


class PersonViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]




    # queryset = Person.objects.all()

    def get_queryset(self):
        pprint(self.request)
        return (Person.objects.all())

    def get_serializer_class(self):
        if self.request.method == "POST" or self.request.method == "PUT":
            return PersonCreateOrUpdateSerializer
        return PersonSerializer

    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name', 'surname',
                     "id_number", "birth_date"]
    # filterset_fields = ["status", "type__certificate_type"]

    ordering_fields = ["name",
                       "id_number", "birth_date", "id_issue_date"]

    permission_classes = [IsStaff]


    def get_serializer_context(self):
        return {"id": self.kwargs.get('pk')}

    # @action(detail=False, methods=["POST"])
    # def secret(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         serializer = ParcelCreateSerializer(data=request.data)
    #         if not serializer.is_valid():
    #             raise serializers.ValidationError({"cart": "This cart is not valid"})
    #         elif not Cart.objects.filter(id=request.data["cart_id"]).exists():
    #             raise serializers.ValidationError({"cart": "This cart does not exists"})

    #         stripe.api_key = settings.STRIPE_SK
    #         cart_id = request.data["cart_id"]
    #         # cart_item = CartItem.objects.get(cart_id= request.kwargs.get('cart_pk'))
    #         # cart = request.data.get('cart')

    #         cart = Cart.objects.get(id=cart_id)

    #         # pprint(cart)

    #         sub_total = settings.PRICE_PARCEL_BY_KG * cart.weigth.quantity

    #         total = round(Decimal((sub_total + Decimal(0.2))) / Decimal(0.975), 2)

    #         tax_list = [0.115 if 1 == "PR" else 0]

    #         fee = (Decimal(total) * Decimal(0.025)) + Decimal(0.2)
    #         # pprint(f"Sub total: {sub_total} Fee: {fee} Total: {total}")

    #         tax = round(sub_total * Decimal(tax_list[0]), 2)

    #         # pprint(f"total: {total}")

    #         # pprint(total)

    #         stripe_total = int(total * 100)
    #         # return 0
    #         intent = stripe.PaymentIntent.create(
    #             amount=stripe_total,
    #             currency="gbp" if cart.country_from.id == 3 else "eur",
    #             automatic_payment_methods={"enabled": True},
    #         )
    #         return Response(
    #             data={"tax": tax, "client_secret": intent.client_secret},
    #             status=status.HTTP_201_CREATED,
    #         )
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
