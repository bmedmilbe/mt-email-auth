
from rest_framework.validators import ValidationError
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from pprint import pprint
from datetime import datetime
from .models import Client, Customer, Destine, Expense, Payment,Product,Sell
from rest_framework import serializers
from pprint import pprint
from django.db.models import Q, Count, Sum

class CustomerSerializer(ModelSerializer):
    first_name = SerializerMethodField(
        method_name="get_first_name")
    last_name = SerializerMethodField(method_name="get_last_name")

    class Meta:
        model = Customer
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
        ]

    def get_first_name(self, customer: Customer):
        return customer.user.first_name

    def get_last_name(self, customer: Customer):
        return customer.user.last_name
class ProductSerializer(ModelSerializer):
    
    class Meta:
        model =Product
        fields = [
            "id",
            "name"
        ]
class DestineSerializer(ModelSerializer):
    
    class Meta:
        model =Destine
        fields = [
            "id",
            "name"
        ]
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


class ClientSerializer(ModelSerializer):
    balance = SerializerMethodField(method_name="get_balance")
    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "tel",
            "balance"
        ]
    def get_balance(self, client: Client):
        out = Sell.objects.filter(client_id=client.id).aggregate(out=Sum("price"))['out'] 
        enter = Payment.objects.filter(client_id=client.id).aggregate(enter=Sum("value"))['enter']
        enter = 0 if not enter else enter
        out = 0 if not out else out

        return enter-out
    



class SellPaymentExpenseSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    client = ClientSerializer()
    product = ProductSerializer()
    customer = CustomerSerializer()
    destine = DestineSerializer()
    from_destine = DestineSerializer()
    quantity = serializers.IntegerField()
    date = serializers.DateTimeField()
    price=serializers.IntegerField()
    value=serializers.IntegerField()
    operation = serializers.CharField()
    

class SellSerializer(ModelSerializer):
    
    client = ClientSerializer()
    product = ProductSerializer()
    class Meta:
        model = Sell
        fields = [
            "id",
            "client",
            "quantity",
            "date",
            "price",
            "value",
            "product",
            "customer",
        ]

class SellCreateSerializer(ModelSerializer):
    
    class Meta:
        model = Sell
        fields = [
            "id",
            "quantity",
            "price",
            "product",
        ]
    def create(self, validated_data):
        data=validated_data
        data['client_id'] = self.context['client_pk']
        data['customer_id'] = self.context['customer_id']
        
        return super().create(data)

class PaymentSerializer(ModelSerializer):
    customer = CustomerSerializer()
    client = ClientSerializer()
    class Meta:
        model = Payment
        fields = [
            "id",
            "value",
            "date",
            "client",
            "customer"
        ]

class PaymentCreateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "value",
        ]
    def create(self, validated_data):
        data=validated_data
        data['client_id'] = self.context['client_pk']
        data['customer_id'] = self.context['customer_id']
        
        return super().create(data)
    
class ExpendCreateSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            "id",
            "value",
        ]
    def create(self, validated_data):
        data=validated_data
        data['destine_id'] = self.context['destine_pk']
        data['customer_id'] = self.context['customer_id']
        
        return super().create(data)
    
class ExpendPaymentCreateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "value",
        ]
    def create(self, validated_data):
        data=validated_data
        data['from_destine_id'] = self.context['destine_pk']
        data['customer_id'] = self.context['customer_id']
        
        return super().create(data)
    

class ExpendSerializer(ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Expense
        fields = [
            "id",
            "value",
            "destine",
            "customer",
        ]
    

