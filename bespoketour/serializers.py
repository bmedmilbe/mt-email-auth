

from rest_framework import serializers
from rest_framework.validators import ValidationError
from bespoketour.models import BespokeTag, Customer, CustomerTag, ProfileTag, ProfileType
from pprint import pprint
class ProfileTypeSimpleSerializer(serializers.ModelSerializer):
    class Meta():
        model = ProfileType
        fields = ['id','title', 'slug', 'image']

class BespokeTagSimpleSerializer(serializers.ModelSerializer):
    class Meta():
        model = BespokeTag
        fields = ['id','title', 'slug', 'image']

class ProfileTagForBespokeTag(serializers.ModelSerializer):
    profile_type = ProfileTypeSimpleSerializer()
    class Meta():
        model = ProfileTag
        fields = ['id','profile_type']

class ProfileTagForProfileType(serializers.ModelSerializer):
    bespoke_tag = BespokeTagSimpleSerializer()
    class Meta():
        model = ProfileTag
        fields = ['id','bespoke_tag']

class ProfileTypeSerializer(serializers.ModelSerializer):
    profile_tags = ProfileTagForProfileType(many=True)
    class Meta():
        model = ProfileType
        fields = ['id','title', 'slug', 'image', 'profile_tags', 'weight']

class BespokeTagSerializer(serializers.ModelSerializer):
    profile_tags = ProfileTagForBespokeTag(many=True)
    class Meta():
        model = BespokeTag
        fields = ['id','title', 'slug', 'image', 'profile_tags']

class MetadataSerializer(serializers.Serializer):
    profile_types = ProfileTypeSerializer(many=True)
    bespoke_tags = BespokeTagSerializer(many=True)

class AddCustomerTagSerializer(serializers.ModelSerializer):
    class Meta():
        model = CustomerTag
        fields = ['id','bespoke_tag']

    def validate_bespoke_tag(self, value:BespokeTag):
        if CustomerTag.objects.filter(customer_id=self.context['customer_id'], bespoke_tag=value).exists():
            raise ValidationError({'bespoke_tag':f"{value.title} is chosen already."})
        return value
        
    def create(self, validated_data):
        customer_id = self.context['customer_id']
        validated_data['customer_id'] = customer_id
        added_tag = super().create(validated_data)
        

        
        tags = BespokeTag.objects.filter(customer_tags__in=CustomerTag.objects.filter(customer_id=customer_id))
        if tags.count() == 3:
            # define the customer profile
           
            profile_value_by_tag = dict()
            profile_slugs = list()
            profile_types = ProfileType.objects.filter(profile_tags__bespoke_tag__in=tags)
           
            for profile_type in list(profile_types): 
                if profile_type.slug not in profile_slugs:
                    profile_slugs.append(profile_type.slug)   
                    profile_value_by_tag[profile_type.slug]=0
                
                profile_value_by_tag[profile_type.slug] = profile_value_by_tag[profile_type.slug] + profile_type.weight
                
               
            weightest = profile_slugs[0]
            for profile_slug in profile_slugs:
                if profile_value_by_tag[weightest] < profile_value_by_tag[profile_slug]:
                    weightest = profile_slug

            chosen_profile = ProfileType.objects.get(slug=weightest)

            Customer.objects.filter(id=customer_id).update(profile_type_id=chosen_profile.pk)

        return added_tag
    
class CustomerTagSerializer(serializers.ModelSerializer):
    bespoke_tag = BespokeTagSerializer()
    class Meta():
        model = CustomerTag
        fields = ['id','customer', 'bespoke_tag']


class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    profile_type = ProfileTypeSerializer()
    customer_tags = CustomerTagSerializer(many=True) 
    class Meta():
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'profile_type','customer_tags']

    def get_first_name(self, obj:Customer):
        return obj.user.first_name
    def get_last_name(self, obj:Customer):
        return obj.user.last_name