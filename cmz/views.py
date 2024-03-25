from django.shortcuts import get_object_or_404, render
from django.db.models.aggregates import Count
from certificates.models import IDType, Street
from certificates.serializers import IDTypeSerializer, StreetSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from .models import  Service, Tour, ImagesTour, Messages, Post, PostDocument, PostFile, PostImages, Section, Team
from .serializers import InformationSerializer, PostImagesSerializer, ServiceSerializer, TourSerializer, ImagesTourSerializer,MessagesSerializer, PostSerializer, SectionSerializer, TeamSerializer
from rest_framework.decorators import action
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
from pprint import pprint
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
# Create your views here.





class SectionViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Section.objects.annotate(
        secreatarys=Count('secreatary_sections')).filter(secreatarys__gt=0)

    serializer_class = SectionSerializer


class TeamViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Team.objects.all().order_by("id")
    serializer_class = TeamSerializer




class TourViewSet(ListModelMixin,RetrieveModelMixin, GenericViewSet):
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]
    # Create a permission to a certain member can post Tour, news, laws
    http_method_names = ['get']

    def get_queryset(self):
        return Tour.objects.filter(active=True).order_by("-date")
        # return Post.objects.filter(user_id=self.request.user.id).order_by("-date")

    def get_serializer_class(self):
        return TourSerializer

    lookup_field = 'slug'

    @action(detail=False, methods=['GET'], http_method_names=['get', 'post', 'patch'], permission_classes=[AllowAny])
    def all(self, request):

        if request.method == 'GET':
            # pprint(request.user.id)
            images = Tour.objects.all().order_by("-date")
            # pprint(images)
            serializer = TourSerializer(images, many=True)
            # pprint(serializer.data)
            return Response(serializer.data)


class ImagesTourViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ImagesTour.objects.filter(tour_id=self.kwargs.get('tour_pk')).prefetch_related("tour").all()

    def get_serializer_class(self):
        return ImagesTourSerializer

    def get_serializer_context(self):
        return {"tour_id": self.kwargs.get('tour_pk')}

    # def get_serializer_context(self):
    #     return {'valid': self.request.user.valid, 'user_id': self.request.user.id}



# class ImagesTourSetViewSet(CreateModelMixin, GenericViewSet):
#     queryset = ImagesTour.objects.prefetch_related("Tour").all()

#     serializer_class = ImagesTourSerializer





# class PostImagesViewSet(ListModelMixin,RetrieveModelMixin, GenericViewSet):

#     def get_queryset(self):
#         return PostImages.objects.filter(post_id=self.kwargs.get('post_pk')).all()

#     def get_serializer_class(self):
#         return PostImagesSerializer

#     def get_serializer_context(self):
#         return {"post_id": self.kwargs.get('post_pk')}


class PostViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    def get_queryset(self):
        return Post.objects.filter(active=True).order_by("-date")

    def get_serializer_class(self):
        return PostSerializer
        

    lookup_field = 'slug'


class PostViewViewSet(RetrieveModelMixin, GenericViewSet):

    def get_queryset(self):
        return Post.objects.select_related('file').all().order_by("-date")

    lookup_field = 'slug'

    def get_serializer_class(self):
        return PostSerializer







class ServiceViewSet(ListModelMixin,RetrieveModelMixin, GenericViewSet):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.order_by("name")
    
    lookup_field = 'slug'



class InformationViewSet(ListModelMixin,RetrieveModelMixin, GenericViewSet):
    serializer_class = InformationSerializer

    def get_queryset(self):
        return InformationSerializer.objects.filter(service_id=self.kwargs.get('service_pk'))
class MessagesViewSet(ModelViewSet):
    serializer_class = MessagesSerializer

    def get_queryset(self):
        return Messages.objects.all()
    
def say_hello(request):
    try:
        # send_mail('subject', 'message', 'edmilbe@gmail.com', ['bob@moshbuy.com'))
        # mail_admins('subject', 'message', html_message='message')
        # message = EmailMessage('subject', 'message', 'edmilbe@gmail.com', ['bob@moshbuy.com'))
        # message.attach_file("core/static/images/contact-us.png")
        # message.send()

        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Mosh Hamedanny'})
        message.send(['john@bonsmabos.com'])

    except BadHeaderError:
        pass

    return render(request, 'core/hello.html', {'msg': 'Email was successfully sent!'})
