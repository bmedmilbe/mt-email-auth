from django.shortcuts import get_object_or_404, render
from django.db.models.aggregates import Count
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .models import   Pathner, Role, Team, Association, AssociationImages, YearGols, Band, Spot, PostImages, Messages, Post, PostDocument
from .serializers import AssociationSerializer, BandSerializer, MessagesSerializer, PathnerSerializer, PostCreateOrUpdateSerializer, PostImagesSerializer, PostSerializer, SpotSerializer, TeamSerializer, YearGolsSerializer
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


class TeamViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Team.objects.all().order_by("role")
    serializer_class = TeamSerializer

class AssociationViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Association.objects.all().order_by("name")
    serializer_class = AssociationSerializer

class BandViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Band.objects.all().order_by("title")
    serializer_class = BandSerializer
    lookup_field = 'slug'

class SpotViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Spot.objects.all().order_by("title")
    serializer_class = SpotSerializer
    lookup_field = 'slug'

class YearGolsViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = YearGols.objects.all().order_by("year")
    serializer_class = YearGolsSerializer

class PathnerViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Pathner.objects.all()
    serializer_class = PathnerSerializer
    
class PostImagesViewSet(ModelViewSet):

    def get_queryset(self):
        return PostImages.objects.filter(post_id=self.kwargs['post_pk']).all()

    def get_serializer_class(self):
        return PostImagesSerializer

    def get_serializer_context(self):
        return {"post_id": self.kwargs['post_pk']}

class PostViewSet(ModelViewSet):
    def get_queryset(self):
        return Post.objects.filter(active=True).order_by("-date")

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        return PostCreateOrUpdateSerializer

    lookup_field = 'slug'


class PostViewViewSet(RetrieveModelMixin, GenericViewSet):

    def get_queryset(self):
        return Post.objects.select_related('file').all().order_by("-date")

    lookup_field = 'slug'

    def get_serializer_class(self):
        return PostSerializer


class MessagesViewSet(ModelViewSet):
    serializer_class = MessagesSerializer

    def get_queryset(self):
        return Messages.objects.all()


def say_hello(request):
    try:
        # send_mail('subject', 'message', 'edmilbe@gmail.com', ['bob@moshbuy.com'])
        # mail_admins('subject', 'message', html_message='message')
        # message = EmailMessage('subject', 'message', 'edmilbe@gmail.com', ['bob@moshbuy.com'])
        # message.attach_file("core/static/images/contact-us.png")
        # message.send()

        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Mosh Hamedanny'})
        message.send(['john@bonsmabos.com'])

    except BadHeaderError:
        pass

    return render(request, 'core/hello.html', {'msg': 'Email was successfully sent!'})
