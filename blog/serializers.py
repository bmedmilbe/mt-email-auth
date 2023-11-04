import html
import mammoth
from pprint import pprint
from rest_framework import serializers
from django.db.transaction import atomic
from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.apps import apps
from django.conf import settings
from .models import Information, SecreatarySection, Secretary, Service, Tour, Post, ImagesTour, Messages, Post, PostDocument, PostFile, PostImages, Role, Section, Team
from core.serializers import UserCreateSerializer
import urllib3
import requests
import requests
import docx2txt
from io import BytesIO
import timeago
from datetime import datetime, timezone
import re


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


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'title']


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ["id", "picture"]

    def create(self, validated_data):
        post_image = validated_data
        post_image['post_id'] = self.context["post_id"]
        return super().create(post_image)


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
                  'posted_at',
                  'date',
                  ]

    def get_posted_at(self, post: Post):
        now = datetime.now(timezone.utc)
        return timeago.format(post.date, now)

    def get_beginnig(self, post: Post):
        url = post.text_file.url
        # url = "http://127.0.0.1:8000/media/camaramz/posts/documents/text_cecab_rubish_1.docx"
        docx = BytesIO(requests.get(url).content)

        # extract text
        text = docx2txt.process(docx)

        return f"{text}"
        with open(path.data, "rb") as docx_file:

            result = mammoth.extract_raw_text(docx_file)
            return result.value.replace('\n', '').strip()  # The raw text

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


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'title']


class TeamSerializer(serializers.ModelSerializer):

    role = RoleSerializer()

    class Meta:
        model = Team
        fields = ['id', 'role',  'name', "image"]


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['name', 'whatsapp', 'subject', 'text']

    def create(self, validated_data):

        pprint(validated_data['subject'])
        secretary_sections = SecreatarySection.objects.filter(
            section__title=validated_data['subject'])
        try:

            # send_mail('subject', 'message', 'edmilbe@gmail.com', ['bob@moshbuy.com'])
            # mail_admins('subject', 'message', html_message='message')
            # message = EmailMessage('subject', 'message', 'edmilbe@gmail.com', ['bob@moshbuy.com'])
            # message.attach_file("core/static/images/contact-us.png")
            # message.send()
            validated_data['sent'] = True
            message = BaseEmailMessage(
                template_name='emails/hello.html',
                context={'text': validated_data['text'],
                         'section': validated_data['subject'],
                         'name': validated_data['name'], 'whatsapp': validated_data['whatsapp']})
            message.send(
                [secretary_section.secretary.user.email for secretary_section in secretary_sections])
            return super().create(validated_data)

        except BadHeaderError:
            pass


class ImagesTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesTour
        fields = ["id", "image"]


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ["id", "service", "question", "information"]


class ServiceSerializer(serializers.ModelSerializer):
    informations = InformationSerializer(many=True)

    class Meta:
        model = Service
        fields = ["id", "name", "slug",
                  "informations",  "picture", "description"]


class TourSerializer(serializers.ModelSerializer):

    images = ImagesTourSerializer(many=True)
    posted_at = serializers.SerializerMethodField(
        method_name="get_posted_at")

    class Meta:
        model = Tour
        fields = ["id", "title", "description",
                  "date", "images", "slug", "posted_at", "location"]

    def get_posted_at(self, post: Post):
        now = datetime.now(timezone.utc)
        return timeago.format(post.date, now)
