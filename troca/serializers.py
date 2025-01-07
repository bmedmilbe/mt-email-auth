
from rest_framework.validators import ValidationError
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from pprint import pprint
from datetime import datetime
from .models import Charge, Customer, Transaction, Friend
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
        ]

class TransactionCreateSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "description",
            "value",
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
        validated_data['completed_by__id'] = self.context['customer_id'] 
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


        