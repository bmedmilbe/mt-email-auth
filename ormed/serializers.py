import mammoth
from pprint import pprint
from rest_framework import serializers
from django.db.transaction import atomic
from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.apps import apps
from django.conf import settings
from .models import Area, Country, Doctor, Gallery, Law, Post, IdType, ImagesGallery, Level, Messages, Post, PostDocument, PostFile, PostImages, Role, Section, Team, UserSection
from core.serializers import UserCreateSerializer
import urllib3
import requests
import requests
import docx2txt
from io import BytesIO
import timeago
from datetime import datetime, timezone
import re
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection, send_mail

def text_to_html_paragraphs(text):
    # First, replace multiple newlines with a single newline,
    # so you don't get empty paragraphs
    text = re.sub(r'\n\s*\n', '\n', text)

    # Split the text into lines
    lines = text.split('\n')

    # Wrap each line in a <p> tag and join them
    return ''.join(f'<p>{line.strip()}</p>\n' for line in lines)

def addPicures(post: Post, html_paragraphs):
     # pprint(len(html_paragraphs.split("@image")))
    text_with_images = ""
    count = 0
    images = post.post_images.all()
    for x in html_paragraphs.split("@image"):
        if len(html_paragraphs.split("@image")) > 1 and count < len(html_paragraphs.split("@image"))-1:
                
            # pprint(f"<img src={post.post_images.all()[count].picture.url} alt={post.title} />")
            
            if len(images) > count:
                text_with_images = f"{text_with_images}{x}<img src={images[count].picture.url} alt={post.title} />" 
                count = count + 1
            else:
                text_with_images = f"{text_with_images}{x}"
        elif len(html_paragraphs.split("@image")) == 1:
            text_with_images = x
        else:
            text_with_images = f"{text_with_images}{x}"

    return text_with_images

def addVideo(post: Post, html_paragraphs):
     # pprint(len(html_paragraphs.split("@image")))
    text_with_video = ""
    count = 0
    videos = post.post_videos.all()
    # pprint(len(videos))
    for x in html_paragraphs.split("@video"):
        if len(html_paragraphs.split("@video")) > 1 and count < len(html_paragraphs.split("@video"))-1:
            if len(videos) > count:
                text_with_video = f"{text_with_video}{x}<div class='video-text embed-responsive embed-responsive-16by9'><iframe class='embed-responsive-item' src={videos[count].video} allowfullscreen></iframe></div>"
                count = count + 1
            else:
                text_with_video = f"{text_with_video}{x}"
        elif len(html_paragraphs.split("@video")) == 1:
            text_with_video = x
        else:
            text_with_video = f"{text_with_video}{x}"

    return text_with_video

# import html
import html




def embed(link):
    return ""
    # return (

    #     '<section className="content-inner-2 wow fadeIn" data-wow-duration="2s" data-wow-delay="0.2s"><div className="container">' +

    #     '<div className="row">' +
    #     '<div className="col-lg-12">' +
    #     '<div className="video-bx style-1 overlay-black-light">' +
    #     '<img rc="https://res.cloudinary.com/dybteyiju/image/upload/v1678362568/alexander-shatov-niUkImZcSP8-unsplash_tkkhw6.jpg" alt="" />' +
    #     '                <div className="video-btn"><a href="#" className="popup-youtube" onClick={() => setOpen(true)}><i className="flaticon-play"></i></a><h2 className="title">Assista o video</h2></div>' +
    #     '             <ModalVideo channel="youtube" autoplay isOpen={isOpen} videoId="{link}" onClose={() => setOpen(false)}/></div>' +
    #     '</div>' +
    #     '</div>' +
    #     '</div>' +
    #     '</section>')

    # return f'<div class="embed-responsive embed-responsive-4by3"><iframe class="embed-responsive-item" src={link} allowfullscreen></iframe></div>'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'title']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'title']


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'title']


class IdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdType
        fields = ['id', 'name']


class DoctorCreateSerializer(serializers.Serializer):
    country = serializers.IntegerField()
    level = serializers.IntegerField()
    area = serializers.IntegerField()
    birth_date = serializers.DateField()
    bio = serializers.CharField()
    id_type = serializers.IntegerField()
    id_number = serializers.IntegerField()
    id_valid = serializers.DateField()

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=255)

    @atomic()
    def create(self, validated_data):
        user = dict()
        user['first_name'] = validated_data['first_name']
        user['last_name'] = validated_data['last_name']
        user['email'] = validated_data['email']
        user['password'] = validated_data['password']
        user['username'] = validated_data['username']
        user['phone'] = validated_data['phone']


        # UserModel = apps.get_model(app_label='core', model_name='user')

        user_serializer = UserCreateSerializer(data=user)

        if not user_serializer.is_valid():
            raise serializers.ValidationError({'user': 'User not valid'})

        user_new = user_serializer.save()

        # pprint(self.context['user_id'])
        # doctor = Doctor.objects.filter(
        #     user_id=self.context['user_id']).first()

        # if doctor:
        #     pprint(doctor.id)
        #     return super().update(doctor, validated_data)

        # validated_data['user_id'] = self.context['user_id']
        # pprint(user_new)
        # pprint(validated_data)
        validated_data['user_id'] = user_new.id
        doctor_new = Doctor.objects.create(
            country_id=validated_data['country'],
            level_id=validated_data['level'],
            area_id=validated_data['area'],
            birth_date=validated_data['birth_date'],
            bio=validated_data['bio'],
            id_type_id=validated_data['id_type'],
            id_number=validated_data['id_number'],
            id_valid=validated_data['id_valid'],
            user_id=user_new.id
        )

        return {'id': doctor_new.id, **validated_data}


class DoctorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "picture"]

    def create(self, validated_data):

        doctor = Doctor.objects.get(id=self.context["doctor_id"])
        doctor.picture = validated_data['picture']
        doctor.save()
        
        return {"id":doctor.id, "picture": doctor.picture}


class DoctorIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "picture"]

    def create(self, validated_data):
        # pprint(validated_data)
        doctor = Doctor.objects.get(id=self.context["doctor_id"])
        doctor.document = validated_data['picture']
        doctor.save()
        
        return {"id":doctor.id, "picture": doctor.document}


class DoctorSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=255)
    

    name = serializers.SerializerMethodField(
        method_name="get_name")
    first_name = serializers.SerializerMethodField(
        method_name="get_first_name")
    last_name = serializers.SerializerMethodField(
        method_name="get_last_name")

    class Meta:
        model = Doctor
        fields = ['id',
                  'country',
                  'level',
                  'area',
                  'birth_date',
                  'bio',
                  'picture',
                  'document',
                  'id_type',
                  'id_number',
                  'id_valid',
                  'name',
                   "first_name", 
                  "last_name",
                  ]

    def get_name(self, doctor: Doctor):
        return f"{doctor.user.first_name} {doctor.user.last_name}"
    def get_first_name(self, doctor: Doctor):
        return f"{doctor.user.first_name}"
    def get_last_name(self, doctor: Doctor):
        name = doctor.user.last_name.split()
        return f"{name[len(name)-1]}"


class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id',
                  'country',
                  'level',
                  'area',
                  'birth_date',
                  'bio',
                  #   'picture',
                  'id_type',
                  'id_number',
                  'id_valid',
                  ]


# class GalleryCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id',
#                   'title',
#                   #   'text',
#                   'description',
#                   'video',
#                   'slug',
#                   'file',
#                   'picture',
#                   ]

#     def validate_slug(self, slug):
#         if not slug:
#             raise serializers.ValidationError({'post': 'Insira o título'})
#         elif Post.objects.filter(slug=slug).exists():
#             raise serializers.ValidationError({'post': 'Publicação já feita'})
#         return slug

#     def create(self, validated_data):
#         if not self.context['valid']:
#             raise serializers.ValidationError(
#                 {'user': 'Tua conta esta sobre avaliação'})
#             pass

#         # pprint(validated_data)
#         post_file = PostFiles.objects.get(id=validated_data['file'].id)

#         path = f'{settings.MEDIA_ROOT}/{post_file.file.name}'

#         with open(path, "rb") as docx_file:
#             result = mammoth.convert_to_html(docx_file)
#             text = result.value

#             validated_data['text'] = text

#             result = mammoth.extract_raw_text(docx_file)
#             validated_data['description'] = result.value  # The raw text

#         validated_data['user_id'] = self.context['user_id']
#         return super().create(validated_data)

#         # with open("a.docx", "rb") as docx_file:


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ["id", "picture"]

    def create(self, validated_data):
        post_image = validated_data
        post_image['post_id'] = self.context["post_id"]
        return super().create(post_image)


class PostCreateOrUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id',
                  'title',
                  'slug',
                  'picture',
                  #   'doctor',
                  'text_file',
                  ]


class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.SerializerMethodField(
    #     method_name="get_owner")
    beginnig = serializers.SerializerMethodField(
        method_name="get_beginnig")

    posted_at = serializers.SerializerMethodField(
        method_name="get_posted_at")

    text = serializers.SerializerMethodField(
        method_name="get_text")

    post_images = PostImagesSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id',
                  'title',
                  'slug',
                  'picture',
                  #   'doctor',
                  'text_file',
                  'post_images',
                  'beginnig',
                  'text',
                  'posted_at'
                  ]

    def get_posted_at(self, post: Post):
        now = datetime.now(timezone.utc)
        return timeago.format(post.date, now)

    def get_beginnig(self, post: Post):
        url = post.text_file.url
        docx = BytesIO(requests.get(url).content)

        # extract text
        text = docx2txt.process(docx)
        
        return f"{text}"
        with open(path.data, "rb") as docx_file:

            result = mammoth.extract_raw_text(docx_file)
            return result.value.replace('\n', '').strip()  # The raw text

    def get_text(self, post: Post):
        url = post.text_file.url
        docx = BytesIO(requests.get(url).content)

        # extract text
        text = docx2txt.process(docx)

        
        html_paragraphs = text_to_html_paragraphs(text).replace("\n", "")
        

        text_with_media = f"{addPicures(post, html_paragraphs)}" 
        text_with_media = f"{addVideo(post, text_with_media)}" 

        
            
        return text_with_media
    


class LawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = ['id', 'title', 'file', 'description']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'title']


class TeamSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    role = RoleSerializer()

    class Meta:
        model = Team
        fields = ['id', 'role',  'doctor']


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'subject', 'text']

    def create(self, validated_data):
        # settings.AUTH_USER_MODEL
        # user_sections = UserSection.objects.filter(section_id=validated_data['subject'])
        User = apps.get_model(app_label='core', model_name='User')
        # pprint(validated_data['subject'])
        users = User.objects.filter(
            usersection__section=validated_data['subject'])
        try:
            email = validated_data['email']
            parthner = parthner = "ORMED"
            convert_to_html_content =  render_to_string(
                                        template_name='emails/message.html',
                                        context={'message': validated_data['text'],
                         'section': validated_data['subject'],
                         'name': validated_data['name'], 'email': validated_data['email']
                                                , 'logo':f"{settings.EMAILS[parthner]['LOGO']}"
                                                }
                                        )
            plain_message = strip_tags(convert_to_html_content) 



            connection = get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAILS[parthner]['EMAIL'],
                password=settings.EMAILS[parthner]['PASSWORD'],
                use_tls=settings.EMAIL_USE_TLS)

            


            # Send an email using the custom connection
            send_mail(
                # 'Subject',
                #        msg_plain,settings.EMAILS[parthner]['EMAIL'], 
                #        [email],
                #        html_message=msg_html,  
                #     #    context={'username': 'John'},
                    
                #       connection=connection
                    
                    
                                
                subject=validated_data['subject'],
                message=plain_message,
                from_email=settings.EMAILS[parthner]['EMAIL'],
                recipient_list=[user.email for user in users],  
                html_message=convert_to_html_content,
                fail_silently=True,   # Optional

                    connection=connection

                    
                    )













            
            # validated_data['sent'] = True
            # message = BaseEmailMessage(
            #     template_name='emails/message.html',
            #     context={'message': validated_data['text'],
            #              'section': validated_data['subject'],
            #              'name': validated_data['name'], 'email': validated_data['email']})
            # message.send([user.email for user in users])
            return super().create(validated_data)

        except BadHeaderError:
            pass


class ImagesGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesGallery
        fields = ["id", "image"]

    def create(self, validated_data):
        image_gallery = validated_data
        image_gallery['gallery_id'] = self.context["gallery_id"]
        return super().create(image_gallery)


class GalleryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ["id", "title", "description", "slug"]


class GallerySerializer(serializers.ModelSerializer):

    images = ImagesGallerySerializer(many=True)
    posted_at = serializers.SerializerMethodField(
        method_name="get_posted_at")

    class Meta:
        model = Gallery
        fields = ["id", "title", "description",
                  "date", "images", "slug", "posted_at"]

    def get_posted_at(self, post: Post):
        now = datetime.now(timezone.utc)
        return timeago.format(post.date, now)


class GalleryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ["id", "title", "description", "slug"]
