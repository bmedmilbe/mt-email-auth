from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from bespoketour.models import BespokeTag, Customer, CustomerTag, ProfileType
from bespoketour.serializers import AddCustomerTagSerializer, CustomerTagSerializer, MetadataSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from bespoketour.serializers import CustomerSerializer
import random
class MetadataViewSet(ViewSet):
    def list(self, request):
        data = {
            "profile_types":ProfileType.objects.prefetch_related("profile_tags").order_by("title"),
            "bespoke_tags":BespokeTag.objects.prefetch_related("profile_tags").order_by("title")
        }

        serializer = MetadataSerializer(data)            
        return Response(serializer.data)
    
class CustomerViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Customer.objects.select_related("profile_type").prefetch_related("customer_tags").filter(user=self.request.user)
        

    
    serializer_class = CustomerSerializer
    
    @action(methods=['get'], detail=False,permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Customer.objects.select_related("profile_type").prefetch_related("customer_tags").get(user=request.user)
        serializer = CustomerSerializer(customer)

        return Response(serializer.data)
    
class CustomerTagViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return CustomerTag.objects.select_related("bespoke_tag").filter(customer__user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCustomerTagSerializer
        return CustomerTagSerializer
    
    def get_serializer_context(self):
        return {'customer_id':Customer.objects.get(user=self.request.user).pk}
    

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCustomerTagSerializer
        return CustomerTagSerializer
    
class MixTagViewSet(ViewSet):
    def list(self, request):
        data = {
            "profile_types":ProfileType.objects.prefetch_related("profile_tags").order_by("title"),
            "bespoke_tags":BespokeTag.objects.prefetch_related("profile_tags").order_by("title")
        }

        serializer = MetadataSerializer(data)
        for profile_types in serializer.data['profile_types']:
            global_list = list()
            for x in random.sample(range(4), k=3):
                internal_list = list()
                for y in range(0,3):
                    internal_list.append(serializer.data['profile_types'][y]['profile_tags'][x])
                global_list.append(internal_list)
    
            
        return Response(global_list)
    
    
