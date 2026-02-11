from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from bespoketour.models import BespokeTag, ProfileType
from bespoketour.serializers import MetadataSerializer

class MetadataViewSet(ViewSet):
    def list(self, request):
        data = {
            "profile_types":ProfileType.objects.order_by("title"),
            "bespoke_tags":BespokeTag.objects.order_by("title")
        }

        serializer = MetadataSerializer(data)
        return Response(serializer.data)
