from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from .models import Airport, Flight, Country, Request
from .serializers import AirportSerializer, FlightSerializer, CountrySerializer, CountryWithAirportsSerializer, RequestCreatSerializer
# Create your views here.
from pprint import pprint
from datetime import datetime
from django.db.models import Q

from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from rest_framework.decorators import action

class CountryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Country.objects.all()
    
    serializer_class = CountrySerializer

    @action(detail=False,methods=['GET'], permission_classes=[AllowAny] )
    def with_airports(self, request, *args, **kwargs):
        
        countries = Country.objects.all() 
        serializers = CountryWithAirportsSerializer(countries, many=True)
        return Response(serializers.data)

    
class AirportViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Airport.objects.all()
    
    serializer_class = AirportSerializer


class FlightViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    @action(detail=False,methods=['GET'], permission_classes=[AllowAny] )
    def prices(self, request, *args, **kwargs):
        # pprint(request.params)
        airport_from = request.GET.get("from")
        airport_to = request.GET.get("to")
        # pprint(f"{airport_from}-{airport_to}")
        now = datetime.now()

        # flights = Flight.objects.filter(Q(date__gt=now.date(), time__gt=now.time(), route=f"{airport_from}-{airport_to}"))
        flights = Flight.objects.filter(Q(date__gt=now.date(), route=f"{airport_from}-{airport_to}"))
        serializers = FlightSerializer(flights, many=True)
        return Response(serializers.data)
    
class RequestViewSet(CreateModelMixin, GenericViewSet):
    queryset = Request.objects.all()
    
    serializer_class = RequestCreatSerializer
    


    


