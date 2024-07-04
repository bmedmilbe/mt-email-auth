from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from .models import ContactOff, Enquire
from .serializers import ContactOffSerializer, EnquireCreatSerializer
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

class EnquireViewSet(CreateModelMixin,  GenericViewSet):
    queryset = Enquire.objects.all()
    
    serializer_class = EnquireCreatSerializer
class ContcatOffViewSet(CreateModelMixin,  GenericViewSet):
    queryset = ContactOff.objects.all()
    
    serializer_class = ContactOffSerializer

   

    


