from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import BasePermission
from rest_framework import status
from pprint import pprint
from django.db.models import Q
from .helpers import get_customer
from .serializers import (ChargeSerializer, 
                          CustomerSerializer, 
                          FriendSerializer, 
                          TransactionCreateSerializer, 
                          TransactionSerializer, 
                          TransactionSetFriendSerializer,
                          TransactionCompleteSerializer,
                          TransactionUncompleteSerializer,

                          )
from rest_framework.decorators import action
# Create your views here.

from .models import Charge, Customer, Friend, Transaction


class IsBoss(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            customer = get_customer(request.user)
            return customer.boss
        return False

class FriendViewSet(ModelViewSet):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    permission_classes = [IsBoss]


class CustomerViewSet(RetrieveModelMixin,GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(user_id=self.request.user)

    serializer_class = CustomerSerializer

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = get_customer(request.user)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

class TransactionViewSet(ModelViewSet):
    
    def get_queryset(self):
        customer = get_customer(self.request.user)
        return Transaction.objects.filter(Q(boss=customer)|Q(completed_by=customer))

    def get_serializer_class(self):

        if self.request.method in ['POST','PATCH']:
            return TransactionCreateSerializer
        return TransactionSerializer
    
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,
                       DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category', 'in_stock']
    search_fields = ['description', 'value', 'friend__name']
    
    filterset_fields = {
        'completed': ['exact'],
        'friend_paid': ['exact'],
    }

    def get_serializer_context(self):
        customer = get_customer(self.request.user)
        return {'boss': customer.boss, 
                    'customer_id': customer.id, 
                    }
       
    
    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def set_friend(self, request, pk=None):
        customer = get_customer(self.request.user)
        context = {'boss': customer.boss}

        transaction = self.get_object()
        
        serializer = TransactionSetFriendSerializer(data=request.data, context=context)
        if serializer.is_valid():
            transaction = serializer.update(transaction,request.data)
            return Response(TransactionSerializer(transaction).data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def complete(self, request, pk=None):
        customer = get_customer(self.request.user)
        context = {'customer_id': customer.id}

        transaction = self.get_object()
        serializer = TransactionCompleteSerializer(data=request.data,context=context)
        transaction = serializer.update(transaction,request.data)
        return Response(TransactionSerializer(transaction).data)
    
    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def uncomplete(self, request, pk=None):
        customer = get_customer(self.request.user)
        context = {'customer_id': customer.id}

        transaction = self.get_object()
        serializer = TransactionUncompleteSerializer(data=request.data, context=context)
        transaction = serializer.update(transaction,request.data)
        return Response(TransactionSerializer(transaction).data)
    

       
    
class ChargeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        customer = get_customer(self.request.user)
        return Charge.objects.filter(Q(boss=customer)|Q(deliver=customer))

    serializer_class = ChargeSerializer

    
    
    
        


    






