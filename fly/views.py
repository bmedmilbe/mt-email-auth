from django.shortcuts import render

from fly.models import Enquire, Flight, Trush
from fly.serializers import EnquireCreateSerializer, EnquireSerializer, FlightSerializer, TrushSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import status, filters, mixins, serializers

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
# from .models import ContactOff, Enquire
# from .serializers import ContactOffSerializer, EnquireCreatSerializer
# Create your views here.
from pprint import pprint
from django.db.models import Q
from datetime import datetime, timedelta, time

from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from rest_framework.decorators import action


class EnquireViewSet(ListModelMixin, CreateModelMixin,  GenericViewSet):
    queryset = Enquire.objects.all()
    
    def get_serializer_class(self):
        pprint(self.request.method)
        if self.request.method == "POST":
            return EnquireCreateSerializer
        return EnquireSerializer
    
class PaginationHundread(PageNumberPagination):
    page_size = 100
    

class FlightsViewSet(ListModelMixin,  GenericViewSet):
    def get_queryset(self):
        # city = self.request.query_params.get("city", 1)

        return Flight.objects.filter(date__gt=datetime.now()).order_by("-date", "airline__name")
        


    
    # queryset = Flight.objects.filter(date__gt=datetime.now()).order_by("-date", "airline__name")
    
    serializer_class = FlightSerializer
    pagination_class = PaginationHundread

    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['city__country','city_to__country', 'city','airline',]

    ordering_fields = ["final_price","date"]

class TrushsViewSet(ListModelMixin, RetrieveModelMixin,  GenericViewSet):
    def get_queryset(self):

        return Trush.objects.all()
            
    serializer_class = TrushSerializer
    pagination_class = PaginationHundread

    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    # filterset_fields = [
    #                     'trushs__city__country',
    #                     'trushs__city_to__country', 
    #                     'trushs__city',
    #                     'trushs__airline',
    #                     ]

    ordering_fields = ["trushs__final_price","trushs__date"]
    

   

    


