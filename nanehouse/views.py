from rest_framework.views import APIView, Response
from pprint import pprint
from uuid import uuid4
from django.shortcuts import render
from rest_framework import status
# Create your views here.
from rest_framework.response import Response
import stripe
from decimal import Decimal, FloatOperation



from django.conf import settings
from rest_framework.decorators import api_view

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action, api_view
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from django.db.models import Q
from cryptography.fernet import Fernet

import hashlib
from .serializers import (
    
    CitySerializer,
   
    StreetSerializer,
   CountrySerializer,
   HouseSerializer,

)

from .models import (
   
    City,
    Customer,
    House,
    Country,
    HouseImage,
    Street,
)

from .helpers import get_customer


from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)




class CityViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = CitySerializer

    queryset = City.objects.all().order_by("name")

class StreetViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Street.objects.all().order_by("name")

    serializer_class =  StreetSerializer
class CountryViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Country.objects.all().order_by("name")

    serializer_class =  CountrySerializer


class HouseViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, GenericViewSet):

    queryset = House.objects.all()
    serializer_class =  HouseSerializer

    

