from djoser.serializers import (
    UserCreateSerializer,
    UserSerializer,
    SetPasswordRetypeSerializer,
    SetUsernameSerializer,
    # SendEmailResetSerializer,
    PasswordResetConfirmRetypeSerializer,
)
from django.db.transaction import atomic
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from pprint import pprint
import random
import string
from django.conf import settings

from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.models import User

# https://stackoverflow.com/questions/2809547/creating-email-templates-with-django

class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "parthner",
            "password",
            "username",
        ]


class UserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
        ]




class PasswordResetConfirmRetypeSerializer( PasswordResetConfirmRetypeSerializer):
    uid = serializers.CharField()
    token = serializers.UUIDField()
    new_password = serializers.CharField()
    re_new_password = serializers.CharField()


    class Meta:
        model = User
        fields = ["uid", "token", "new_password", "re_new_password"]

    def create(self, validated_data):

        if validated_data['new_password'] != validated_data['re_new_password']:
            serializers.ValidationError("Password not equal")

        email = validated_data['email']
        ct = ContentType.objects.get_for_id(50)
        UserTokens = ct.model_class()
        users = UserTokens.objects.filter(token=validated_data['token'])
        if users.exists:
            user = User.objects.get(email=users.first().email)
            user.set_password(validated_data['re_new_password'])  # Replace with the desired new password
            user.save()
            users.delete()
        # reset_instance = UserTokens.objects.create(email=email)

        return validated_data


class SetPasswordRetypeSerializer(SetPasswordRetypeSerializer):
    class Meta:
        model = User
        fields = ["id", "current_password", "new_password", "re_new_password"]


class SetUsernameSerializer(SetUsernameSerializer):
    class Meta:
        model = User
        fields = ["id", "new_email", "re_new_email", "current_password"]
