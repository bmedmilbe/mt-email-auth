# Create your views here.

# from msilib.schema import File

import stripe

import os
from io import BytesIO
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from django.db.models import Q
from django.shortcuts import render

from . import serializers
from . import models
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status, filters, mixins
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
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name', 'matches__identity__name']
class Pagination300(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 5000

class IdentityViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = models.Identity.objects.all()
    serializer_class = serializers.IdentityFirstSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name']
    pagination_class = Pagination300
    
    # filterset_fields = ["status", "type__certificate_type"]

    # filterset_fields = {
    #     'status': ['exact'],
    #     'type__certificate_type': ['exact', 'gt', 'lte'],
    # }

    # ordering_fields = ['number', "main_person__name",
    #                    "main_person__id_number", "main_person__birth_date", "date_issue"]

class OrderViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = models.Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.OrderCreateSerializer
        return serializers.OrderFirstSerializer

