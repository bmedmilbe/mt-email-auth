from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import BasePermission
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import status, filters, mixins, serializers
from pprint import pprint
from django.db.models import Q, Count, Sum
from .helpers import get_customer
from itertools import chain
from .serializers import (
 
                          CustomerSerializer,
                          DestineSerializer,
                          ExpendCreateSerializer,
                          ExpendPaymentCreateSerializer,
                          ExpendSerializer, 
                          ProductSerializer,
                          ClientSerializer,
                          SellPaymentExpenseSerializer,
                          SellSerializer,
                          SellCreateSerializer,
                          PaymentCreateSerializer,
                          PaymentSerializer

                          )
from rest_framework.decorators import action
# Create your views here.

from .models import Client, Customer, Destine, Expense,  Product, Sell,Payment, SellPaymentExpense


class Pagination300(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 5000

class ProductsViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by("name")
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination300
class DestinesViewSet(ModelViewSet):
    serializer_class = DestineSerializer
    queryset = Destine.objects.order_by("name")
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination300

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def balance(self, request, pk=None):

        destine_id=self.kwargs.get("pk")
        out = Expense.objects.filter(destine_id=destine_id,).aggregate(out=Sum("value"))
        enter = Payment.objects.filter(from_destine_id=destine_id).aggregate(enter=Sum("value"))
        
        return Response(enter | out)


class ClientsViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.order_by("name")
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination300

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def balance(self, request, pk=None):

       
        client_id=self.kwargs.get("pk")
        out = Sell.objects.filter(client_id=client_id).aggregate(out=Sum("price"))
        enter = Payment.objects.filter(client_id=client_id).aggregate(enter=Sum("value"))
        
        return Response(enter | out)

   


class CustomerViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.all().order_by("user__first_name")

    serializer_class = CustomerSerializer

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = get_customer(request.user)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    

class PaymentsByClientViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PaymentCreateSerializer
        return SellPaymentExpenseSerializer

    def get_serializer_context(self):
        client_pk = self.kwargs.get('client_pk')
        customer = get_customer(self.request.user)
        return {'customer_id': customer.id, 'client_pk': client_pk}
    def get_queryset(self):

        queries = list(Sell.objects.filter(client_id=self.kwargs.get('client_pk')).order_by('-date')) \
            + list(Payment.objects.filter(client_id=self.kwargs.get('client_pk')).order_by('-date')) 
        queries = sorted(queries, key=lambda sell: sell.date)[::-1]
        return [SellPaymentExpense(qu) for qu in queries] 
    
    permission_classes = [IsAuthenticated]

    
    
class PaymentsAllViewSet(ModelViewSet):

    serializer_class = PaymentSerializer

    queryset = Payment.objects.all()
    
    permission_classes = [IsAuthenticated]

def get_date(item):
    # You need to define how to access the date attribute
    # based on the model of the 'item'
    if isinstance(item, Sell):
        return item.date  # Replace with the actual date field name in ModelA
    elif isinstance(item, Payment):
        return item.date  # Replace with the actual date field name in ModelB
    elif isinstance(item, Expense):
        return item.date  # Replace with the actual date field name in ModelB
    return None  # Handle cases where there's no date


class SellsByClientViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.request.method == "POST":
            return SellCreateSerializer
        return SellPaymentExpenseSerializer

    def get_serializer_context(self):
        client_pk = self.kwargs.get('client_pk')
        customer = get_customer(self.request.user)
        return {'customer_id': customer.id, 'client_pk': client_pk}
    def get_queryset(self):

        
        # return Sell.objects.filter(client_id=self.kwargs.get('client_pk')) 
       
       
        # queries = list(Sell.objects.filter(client_id=self.kwargs.get('client_pk')).order_by('-date')) + list(Payment.objects.filter(client_id=self.kwargs.get('client_pk')).order_by('-date')) 
        
        
        # queries = sorted(queries, key=lambda sell: sell.date)

        # return [SellPaymentExpense(qu) for qu in queries]
        queryset_a = Sell.objects.filter(client_id=self.kwargs.get('client_pk'))
        queryset_b = Payment.objects.filter(client_id=self.kwargs.get('client_pk'))
        combined_results_iterable = chain(queryset_a, queryset_b)
        combined_results_list = list(combined_results_iterable)
        sorted_combined_results = sorted(combined_results_list, key=get_date, reverse=True)
        return [SellPaymentExpense(qu) for qu in sorted_combined_results]

    
    pagination_class = PageNumberPagination
    
    
class SellsPaymentsExpensesViewSet(ModelViewSet):

    def get_serializer_class(self):
        # if self.request.method == "POST":
        #     return SellCreateSerializer
        return SellPaymentExpenseSerializer

    def get_serializer_context(self):
        customer = get_customer(self.request.user)
        return {'customer_id': customer.id}
    def get_queryset(self):

        
        # return Sell.objects.filter(client_id=self.kwargs.get('client_pk')) 
       
       
        # queries = list(Sell.objects.filter(client_id=self.kwargs.get('client_pk')).order_by('-date')) + list(Payment.objects.filter(client_id=self.kwargs.get('client_pk')).order_by('-date')) 
        
        
        # queries = sorted(queries, key=lambda sell: sell.date)

        # return [SellPaymentExpense(qu) for qu in queries]
        
        queryset_b = Payment.objects.all()
        queryset_c = Expense.objects.all()
        combined_results_iterable = chain( queryset_b, queryset_c)
        combined_results_list = list(combined_results_iterable)
        sorted_combined_results = sorted(combined_results_list, key=get_date, reverse=True)
        return [SellPaymentExpense(qu) for qu in sorted_combined_results]

    
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def balance(self, request, pk=None):

       
        
        out = Expense.objects.all().aggregate(out=Sum("value"))
        enter = Payment.objects.all().aggregate(enter=Sum("value"))

        return Response(enter | out)
    
    


   
    

class SellsAllViewSet(ModelViewSet):
    
    def get_queryset(self):
        #add payment and expense
        queries = list(Sell.objects.order_by('-date')) + list(Payment.objects.order_by('-date')) + list(Expense.objects.order_by('-date'))

        return [SellPaymentExpense(qu) for qu in queries]


    def get_serializer_class(self):
        return SellPaymentExpenseSerializer
    
    # permission_classes = [IsAuthenticated]


    # filter_backends = [SearchFilter,
    #                    DjangoFilterBackend, OrderingFilter]
    # search_fields = ['client__name', 'client__tel', 'product__name']
    # # filterset_fields = ["status", "type__certificate_type"]

    # filterset_fields = {
    #     'client__id': ['exact'],
    #     'product__id': ['exact'],

    # }

    # ordering_fields = ['date']

    # pagination_class = PageNumberPagination
    
    
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def balance(self, request, pk=None):
        production = Sell.objects.aggregate(production=Sum("price"))
        enter = Payment.objects.aggregate(enter=Sum("value"))
        expense = Expense.objects.aggregate(expense=Sum("value"))
        
        return Response(enter | production | expense)
    
class ExpensesViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ExpendCreateSerializer
        return SellPaymentExpenseSerializer

    def get_serializer_context(self):
        destine_pk = self.kwargs.get('destine_pk')
        customer = get_customer(self.request.user)
        return {'customer_id': customer.id, 'destine_pk': destine_pk}
    def get_queryset(self):

        # return Expense.objects.filter(destine_id=self.kwargs.get('destine_pk'))
        queryset_a = Expense.objects.filter(destine_id=self.kwargs.get('destine_pk'))
        queryset_b = Payment.objects.filter(from_destine_id=self.kwargs.get('destine_pk'))
        combined_results_iterable = chain(queryset_a, queryset_b)
        combined_results_list = list(combined_results_iterable)
        sorted_combined_results = sorted(combined_results_list, key=get_date, reverse=True)
        return [SellPaymentExpense(qu) for qu in sorted_combined_results]

    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

class ExpensePaymentsViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ExpendPaymentCreateSerializer
        return SellPaymentExpenseSerializer

    def get_serializer_context(self):
        destine_pk = self.kwargs.get('destine_pk')
        customer = get_customer(self.request.user)
        return {'customer_id': customer.id, 'destine_pk': destine_pk}
    def get_queryset(self):

        # return Expense.objects.filter(destine_id=self.kwargs.get('destine_pk'))
        queryset_a = Expense.objects.filter(destine_id=self.kwargs.get('destine_pk'))
        queryset_b = Payment.objects.filter(from_destine_id=self.kwargs.get('destine_pk'))
        combined_results_iterable = chain(queryset_a, queryset_b)
        combined_results_list = list(combined_results_iterable)
        sorted_combined_results = sorted(combined_results_list, key=get_date, reverse=True)
        return [SellPaymentExpense(qu) for qu in sorted_combined_results]

    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination


    
    


    
    
    

        
    
    
    