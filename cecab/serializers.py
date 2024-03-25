import mammoth
from pprint import pprint
from rest_framework import serializers
from django.db.transaction import atomic
from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.apps import apps
from django.conf import settings
from .models import  Association, AssociationImages, Band, Pathner, Post, Messages, Post, PostDocument, PostImages, Role, Spot, Team,  YearGols
from core.serializers import UserCreateSerializer
from django.core.files import File
import timeago
from datetime import datetime, timezone
from io import BytesIO
import docx2txt
import requests
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


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'title']

class TeamSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    class Meta:
        model = Team
        fields = ['id', 'name', 'picture', 'role']
class PathnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pathner
        fields = ['id', 'title', 'picture']


# class MessagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Messages
#         fields = ['name', 'email', 'subject', 'text']

#     def create(self, validated_data):
#         # settings.AUTH_USER_MODEL
#         # user_sections = UserSection.objects.filter(section_id=validated_data['subject'])
#         User = apps.get_model(app_label='core', model_name='User')
#         pprint(validated_data['subject'])
#         users = User.objects.filter(
#             is_staff=True, is_active=True)
#         try:

#             validated_data['sent'] = True
#             message = BaseEmailMessage(
#                 template_name='emails/hello.html',
#                 context={'text': validated_data['text'],
#                          'section': validated_data['subject'],
#                          'name': validated_data['name'], 'email': validated_data['email']})
#             message.send([user.email for user in users])
#             return super().create(validated_data)

#         except BadHeaderError:
#             pass

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'subject', 'text']

    def create(self, validated_data):
        
        try:
            email = validated_data['email']
            parthner = parthner = "CECAB"
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
                recipient_list=[email],  
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



class AssociationImagesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AssociationImages
        fields = ['id', 'associaton', 'image']

class AssociationSerializer(serializers.ModelSerializer):
    district_name = serializers.SerializerMethodField(
        method_name="get_district")
    images = AssociationImagesSerializer(many=True)
    class Meta:
        model = Association
        fields = ['id', 'name', 'registered', 'address', 'president_name', 'number_of_associated', 'picture', 'images',  'district_name']
    def get_district(self, association: Association):
        return association.district.name

class YearGolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearGols
        fields = ['id', 'year', 'associations', 'agricultors', 'products']

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'title', 'link', 'picture']

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ['id', 'title', 'created_at', 'link', 'picture']


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
        # path = post.text_file.path
        # path = post.text_file.url


        # with open(path, "rb") as docx_file:

        #     result = mammoth.extract_raw_text(docx_file)
        #     return result.value.replace('\n', '').strip()  # The raw text
        
        url = post.text_file.url
        # url = "http://127.0.0.1:8000/media/camaramz/posts/documents/text_cecab_rubish_1.docx"
        docx = BytesIO(requests.get(url).content)

        # extract text
        text = docx2txt.process(docx)

        return f"{text}"

    # def get_text(self, post: Post):
    #     # path = post.text_file.path
    #     path = post.text_file.url



    #     with open(path, "rb") as docx_file:
    #         result = mammoth.convert_to_html(docx_file)
    #         text = result.value
    #         return text
    def get_text(self, post: Post):

        url = post.text_file.url
        # url = "http://127.0.0.1:8000/media/camaramz/posts/documents/text_cecab_rubish_1.docx"

        docx = BytesIO(requests.get(url).content)

        # extract text
        text = docx2txt.process(docx)

        html_paragraphs = text_to_html_paragraphs(text).replace("\n", "")

        text_with_media = f"{addPicures(post, html_paragraphs)}"
        text_with_media = f"{addVideo(post, text_with_media)}"

        return text_with_media



