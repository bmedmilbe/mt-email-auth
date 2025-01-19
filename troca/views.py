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
from django.db.models import Q, Count, Sum
from .helpers import get_customer
from .serializers import (ChargeCreateSerializer, ChargeSerializer, 
                          CustomerSerializer, 
                          FriendSerializer, FriendTransactionsSerializer, PaymentForFriendCreateSerializer, PaymentForFriendSerializer, 
                          TransactionCreateSerializer, TransactionDeleteSerializer, 
                          TransactionSerializer, 
                          TransactionSetFriendSerializer,
                          TransactionCompleteSerializer,
                          TransactionUncompleteSerializer,
                          TransactionChargeSerializer

                          )
from rest_framework.decorators import action
# Create your views here.

from .models import Charge, Customer,  Friend, FriendPayment, Transaction


class IsBoss(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            customer = get_customer(request.user)
            return customer.boss
        return False

class FriendViewSet(ModelViewSet):
    serializer_class = FriendTransactionsSerializer
    queryset = Friend.objects.all()
    permission_classes = [IsBoss]

    @action(detail=False, methods=['get'], permission_classes=[IsBoss])
    def balance(self, request, pk=None):
        boss_id=request.query_params.get("boss")
        friend_id=request.query_params.get("friend")
        enter = FriendPayment.objects.filter(Q(friend_id=friend_id),Q(boss_id=boss_id)).aggregate(enter=Sum("value"))
        out = Transaction.objects.filter(Q(friend_id=friend_id),Q(boss_id=boss_id)).aggregate(out=Sum("value"))

    
        return Response(enter | out)

class FriendPaymentViewSet(ModelViewSet):
    # serializer_class = PaymentForFriendSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PaymentForFriendCreateSerializer
        return PaymentForFriendSerializer

    def get_serializer_context(self):
        customer = get_customer(self.request.user)
        return {'boss_id': customer.id, "pk":self.kwargs.get('friend_pk')}
    def get_queryset(self):

        # return super().get_queryset()
        pprint(self.kwargs)
        return FriendPayment.objects.filter(friend_id=self.kwargs.get('friend_pk'))
    
    permission_classes = [IsBoss]



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

class TransactionViewSet(ModelViewSet):
    
    def get_queryset(self):
        customer = get_customer(self.request.user)
        return Transaction.objects.filter(Q(boss=customer)|Q(completed_by=customer)).order_by('-id')

    def get_serializer_class(self):
        # pprint(self.request.method)
        if self.request.method in ['POST','PATCH']:
            return TransactionCreateSerializer
        
        return TransactionSerializer
    
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,
                       DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['boss', 'is_charge', 'completed', 'completed_by','friend', 'friend_paid']
    search_fields = ['description', 'value', 'friend__name']
    
    # filterset_fields = {
    #     'completed': ['exact'],
    #     'friend_paid': ['exact'],
    # }

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
    def set_charge(self, request, pk=None):
        customer = get_customer(self.request.user)
        context = {'boss': customer.boss}

        transaction = self.get_object()
        
        serializer = TransactionChargeSerializer(data=request.data, context=context)
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
    @action(detail=True, methods=['delete'], permission_classes=[IsAuthenticated])
    def delete(self, request, pk=None):
        customer = get_customer(self.request.user)
        context = {'customer_id': customer.id,'boss': customer.boss}

        transaction = self.get_object()
        serializer = TransactionDeleteSerializer(data=request.data,context=context)
        transaction = serializer.delete(transaction)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def uncomplete(self, request, pk=None):
        customer = get_customer(self.request.user)
        context = {'customer_id': customer.id}

        transaction = self.get_object()
        serializer = TransactionUncompleteSerializer(data=request.data, context=context)
        transaction = serializer.update(transaction,request.data)
        return Response(TransactionSerializer(transaction).data)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def total_i_charged(self, request, pk=None):
        customer = get_customer(self.request.user)
        deliver_id=request.query_params.get("deliver")
        charges = Transaction.objects.filter(Q(deliver_id=deliver_id),Q(boss=customer), is_charge=True).aggregate(total=Sum("value"))
        # pprint(charges)
        # serializer = ChargeSerializer(charges, many=True)
        return Response(charges)
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def total_i_got(self, request, pk=None):
        customer = get_customer(self.request.user)
        boss_id=request.query_params.get("boss")
        charges = Transaction.objects.filter(Q(completed_by=customer),Q(boss_id=boss_id), is_charge=True).aggregate(total=Sum("value"))
        # pprint(charges)
        # serializer = ChargeSerializer(charges, many=True)
        return Response(charges)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def balance(self, request, pk=None):
        boss_id=request.query_params.get("boss")
        deliver_id=request.query_params.get("deliver")
        enter = Transaction.objects.filter(Q(completed_by_id=deliver_id),Q(boss_id=boss_id), is_charge=True).aggregate(enter=Sum("value"))
        out = Transaction.objects.filter(Q(completed_by_id=deliver_id),Q(boss_id=boss_id), completed=True).aggregate(out=Sum("value"))

    
        return Response(enter | out)
    
    

        
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def total_i_delivered(self, request, pk=None):
        customer = get_customer(self.request.user)
        boss_id=request.query_params.get("boss")
        total = Transaction.objects.filter(Q(completed_by=customer),Q(boss_id=boss_id), is_charge=False, completed=True).aggregate(total=Sum("value"))
        # pprint(charges)
        # serializer = ChargeSerializer(charges, many=True)
        return Response(total)
    
    
   
       
    
class ChargeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        customer = get_customer(self.request.user)

        return Charge.objects.filter(Q(boss=customer)|Q(completed_by=customer))

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            return ChargeCreateSerializer

        return ChargeSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def total_i_got(self, request, pk=None):
        customer = get_customer(self.request.user)
        charges = Charge.objects.filter(completed_by=customer).aggregate(total=Sum("value"))
        # pprint(charges)
        # serializer = ChargeSerializer(charges, many=True)
        return Response(charges)
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def total_i_gave(self, request, pk=None):
        customer = get_customer(self.request.user)
        charges = Charge.objects.filter(boss=customer).aggregate(total=Sum("value"))
        # pprint(charges)
        # serializer = ChargeSerializer(charges, many=True)
        return Response(charges)
    
    def get_serializer_context(self):
        customer = get_customer(self.request.user)
        if customer:
            return {'boss': customer.boss, 'boss_id': customer.id}
        return {'boss': False}
    

    
    
    
        


    






