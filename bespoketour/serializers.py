

from rest_framework import serializers
from bespoketour.models import BespokeTag, ProfileTag, ProfileType

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
        fields = ['id','title', 'slug', 'image', 'profile_tags']

class BespokeTagSerializer(serializers.ModelSerializer):
    profile_tags = ProfileTagForBespokeTag(many=True)
    class Meta():
        model = BespokeTag
        fields = ['id','title', 'slug', 'image', 'profile_tags']

class MetadataSerializer(serializers.Serializer):
    profile_types = ProfileTypeSerializer(many=True)
    bespoke_tags = BespokeTagSerializer(many=True)
