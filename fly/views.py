from django.shortcuts import render

from fly.models import Enquire, Flight
from fly.serializers import EnquireCreateSerializer, EnquireSerializer, FlightSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
# from .models import ContactOff, Enquire
# from .serializers import ContactOffSerializer, EnquireCreatSerializer
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


class EnquireViewSet(ListModelMixin, CreateModelMixin,  GenericViewSet):
    queryset = Enquire.objects.all()
    
    def get_serializer_class(self):
        pprint(self.request.method)
        if self.request.method == "POST":
            return EnquireCreateSerializer
        return EnquireSerializer

class FlightsViewSet(ListModelMixin,  GenericViewSet):
    queryset = Flight.objects.order_by("-date", "airline__name")
    
    serializer_class = FlightSerializer

   

    


