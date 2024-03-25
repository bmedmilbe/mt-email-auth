from django.shortcuts import get_object_or_404, render
from django.db.models.aggregates import Count
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from .models import Area, Country, Doctor, Gallery, IdType, ImagesGallery, Law, Level, Messages, Post, PostDocument, PostFile, PostImages, Section, Team
from .serializers import AreaSerializer, CountrySerializer, DoctorCreateSerializer, DoctorIDSerializer, DoctorImageSerializer, DoctorSerializer, DoctorUpdateSerializer, GallerySerializer, GalleryUpdateSerializer, IdTypeSerializer, ImagesGallerySerializer,  LawSerializer, LevelSerializer, DoctorSerializer, MessagesSerializer, GalleryCreateSerializer, PostCreateOrUpdateSerializer,  PostSerializer, SectionSerializer, TeamSerializer
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


class CountryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Country.objects.all().order_by("name")
    serializer_class = CountrySerializer


class LevelViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Level.objects.all().order_by("title")
    serializer_class = LevelSerializer


class AreaViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Area.objects.all().order_by("title")
    serializer_class = AreaSerializer


class SectionViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Section.objects.annotate(
        users=Count('user_sections')).filter(users__gt=0)

    serializer_class = SectionSerializer


class IdTypeViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = IdType.objects.all().order_by("name")
    serializer_class = IdTypeSerializer


class TeamViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Team.objects.all().order_by("id")
    serializer_class = TeamSerializer


class DoctorViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return Doctor.objects.filter(user_id=self.request.user.id)
        return Doctor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DoctorCreateSerializer
        elif self.request.method == 'PUT':
            return DoctorUpdateSerializer
        return DoctorSerializer

    @action(detail=False, methods=['GET', 'PATCH', 'DELETE'], permission_classes=[IsAuthenticated])
    def me(self, request):
        if request.method == 'GET':
            pprint(request.user.id)
            doctor = Doctor.objects.filter(user_id=request.user.id).first()
            if doctor:
                serializer = DoctorSerializer(doctor)
                return Response(serializer.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PATCH':
            # query for the UserSettings object
            # doctor = Doctor.objects.filter(user_id=request.user.id).first()
            
            doctor = Doctor.objects.filter(user_id=request.user.id).first()

            instance = get_object_or_404(Doctor, pk=doctor.id)
            serializer = DoctorSerializer(instance, data=request.data)
            pprint(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            # query for the UserSettings object
            instance = get_object_or_404(Doctor, pk=request.user.id)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}


class GalleryViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]
    # Create a permission to a certain member can post gallery, news, laws
    http_method_names = ['get']

    def get_queryset(self):
        return Gallery.objects.filter(active=True).order_by("-date")
        # return Post.objects.filter(user_id=self.request.user.id).order_by("-date")

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return GalleryCreateSerializer
        elif self.request.method == 'PUT':
            return GalleryUpdateSerializer
        return GallerySerializer

    lookup_field = 'slug'

    @action(detail=False, methods=['GET'], http_method_names=['get', 'post', 'patch'], permission_classes=[AllowAny])
    def all(self, request):

        if request.method == 'GET':
            # pprint(request.user.id)
            images = Gallery.objects.all().order_by("-date")
            # pprint(images)
            serializer = GallerySerializer(images, many=True)
            # pprint(serializer.data)
            return Response(serializer.data)


class ImagesGalleryViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ImagesGallery.objects.filter(gallery_id=self.kwargs['gallery_pk']).prefetch_related("gallery").all()

    def get_serializer_class(self):
        return ImagesGallerySerializer

    def get_serializer_context(self):
        return {"gallery_id": self.kwargs['gallery_pk']}

    # def get_serializer_context(self):
    #     return {'valid': self.request.user.valid, 'user_id': self.request.user.id}


class LawsViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get_queryset(self):
        return Law.objects.all()

    def get_serializer_class(self):
        return LawSerializer


# class ImagesGallerySetViewSet(CreateModelMixin, GenericViewSet):
#     queryset = ImagesGallery.objects.prefetch_related("gallery").all()

#     serializer_class = ImagesGallerySerializer


class DoctorImageViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.filter(id=self.kwargs['doctor_pk']).all()

    def get_serializer_class(self):
        return DoctorImageSerializer

    def get_serializer_context(self):
        return {"doctor_id": self.kwargs['doctor_pk']}


class DoctorIDViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.filter(doctor_id=self.kwargs['doctor_pk']).all()

    def get_serializer_class(self):
        return DoctorIDSerializer

    def get_serializer_context(self):
        return {"doctor_id": self.kwargs['doctor_pk']}


class PostImagesViewSet(ModelViewSet):

    def get_queryset(self):
        return PostImages.objects.filter(post_id=self.kwargs['post_pk']).all()

    def get_serializer_class(self):
        return DoctorImageSerializer

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
