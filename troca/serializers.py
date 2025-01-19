
from rest_framework.validators import ValidationError
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from pprint import pprint
from datetime import datetime
from .models import Charge, Customer, FriendPayment,  Transaction, Friend
from rest_framework import serializers
from pprint import pprint
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
            "boss",
            "is_deliver"
        ]

    def get_first_name(self, customer: Customer):
        return customer.user.first_name

    def get_last_name(self, customer: Customer):
        return customer.user.last_name
class FriendSerializer(ModelSerializer):
    
    class Meta:
        model =Friend
        fields = [
            "id",
            "name"
        ]

class FriendSerializer(ModelSerializer):
    
    class Meta:
        model =Friend
        fields = [
            "id",
            "name"
        ]


class TransactionSerializer(ModelSerializer):
    boss = CustomerSerializer()
    completed_by = CustomerSerializer()
    friend = FriendSerializer()
    class Meta:
        model = Transaction
        fields = [
            "id",
            "description",
            "value",
            "date",
            "boss",
            "completed",
            "completed_date",
            "completed_by",
            "friend",
            "friend_paid",
            "is_charge",
        ]

class PaymentForFriendSerializer(ModelSerializer):

    class Meta:
        model = FriendPayment
        fields = [
            "id",
            "value",
            "date",
        ]
class PaymentForFriendCreateSerializer(ModelSerializer):

    class Meta:
        model = FriendPayment
        fields = [
            "id",
            "value",
            "description",
            "date",
        ]
    def create(self, validated_data):
        data=validated_data
        data['friend_id'] = self.context['pk']
        data['boss_id'] = self.context['boss_id']
        
        return super().create(data)

class TransactionForFriendSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            "id",
            "description",
            "value",
            "date",
            "completed",
            "completed_date",
            "friend_paid",
        ]
class FriendTransactionsSerializer(ModelSerializer):
    transactions = TransactionForFriendSerializer(many=True)
    payments = PaymentForFriendSerializer(many=True)
    class Meta:
        model =Friend
        fields = [
            "id",
            "name",
            "transactions",
            "payments"
        ]
class TransactionDeleteSerializer(ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = [
            "id",
         
        ]
    def delete(self, instance):
        if not  self.context['boss']:
            raise ValidationError('You are not boss!')
        return Transaction.objects.get(id=instance.id).delete()

class TransactionCreateSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "description",
            "value",
            "friend",
            "is_charge",
            "completed_by"
        ]
    
    def create(self, validated_data):
        if not  self.context['boss']:
            raise ValidationError('You are not boss!')
        
        validated_data['boss_id'] = self.context['customer_id']
        return super().create(validated_data)
    
    def destroy(self, instance, request):
        if not  self.context['boss']:
            raise ValidationError('You are not boss!')
        super().destroy(instance, request)
    
    
        
class TransactionSetFriendSerializer(ModelSerializer):
    friend = serializers.IntegerField()
    friend_paid = serializers.BooleanField()
    
    def validate_friend(self, value):
        if not value:
            raise ValidationError('Friend is required')
        
        elif not Friend.objects.filter(pk=value).exists():
            raise ValidationError('Friend does not exist')
    
    class Meta:
        model = Transaction
        fields = [
            "id",
            "friend",
            "friend_paid"
        ]
    def update(self, instance, validated_data):
        if not  self.context['boss']:
            raise ValidationError('You are not boss!')
        
        data = validated_data
        validated_data = dict()
        validated_data['friend_id'] = data['friend']
        validated_data['friend_paid'] = data['friend_paid']
        return super().update(instance, validated_data)
        
class TransactionChargeSerializer(ModelSerializer):
    deliver = serializers.IntegerField()
    
    def validate_deliver(self, value):
        if not value:
            raise ValidationError('Deliver is required')
        
        elif not Customer.objects.filter(pk=value).exists():
            raise ValidationError('Deliver does not exist')
    
    class Meta:
        model = Transaction
        fields = [
            "id",
            "deliver",
        ]
    def update(self, instance, validated_data):
        if not  self.context['boss']:
            raise ValidationError('You are not boss!')
        
        data = validated_data
        validated_data = dict()
        validated_data['completed_by_id'] = data['deliver']
        validated_data['is_charge'] = True
        return super().update(instance, validated_data)
    

class TransactionUnsetFriendSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
        ]
    
    def update(self, instance, validated_data):
        if not  self.context['boss']:
            raise ValidationError('You are not boss!')
        
        validated_data = dict()
        validated_data['friend'] = None
        validated_data['friend_paid'] = False
        return super().update(instance, validated_data)

class TransactionCompleteSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id"
        ]
    def update(self, instance, validated_data):
        validated_data = dict()
        validated_data['completed_by_id'] = self.context['customer_id'] 
        validated_data['completed'] = True
        validated_data['completed_date'] = datetime.now()
        return super().update(instance, validated_data)
    
    
    
class TransactionUncompleteSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id"
        ]
    def update(self, instance, validated_data):
        validated_data = dict()
        validated_data['completed'] = False
        return super().update(instance, validated_data)
    

class ChargeSerializer(ModelSerializer):
    boss = CustomerSerializer()
    deliver = CustomerSerializer()
    class Meta:
        model = Charge
        fields = [
            "id",
            "value",
            "date",
            "boss",
            "deliver", 
        ]
    def update(self, instance, validated_data):

        if not  self.context['boss']:
            raise ValidationError('You are not boss!')
        
        return super().update(instance, validated_data)

class ChargeCreateSerializer(ModelSerializer):
    
    class Meta:
        model = Charge
        fields = [
            "id",
            "value",
            "deliver", 
        ]
    def create(self,  validated_data):

        if not self.context['boss']:
            raise ValidationError('You are not boss!')
        
        validated_data['boss_id'] = self.context['boss_id']
        return super().create(validated_data)
    
    def create(self,instance,  validated_data):

        if not self.context['boss']:
            raise ValidationError('You are not boss!')
        
        return super().update(instance,validated_data)


        