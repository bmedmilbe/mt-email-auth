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




class PasswordResetConfirmRetypeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "uid", "token", "new_password", "re_new_password"]

    def create(self, validated_data):
        email = validated_data['email']
        UserTokens.objects.filter(email=email).delete()
        reset_instance = UserTokens.objects.create(email=email)

        return reset_instance


class SetPasswordRetypeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "current_password", "new_password", "re_new_password"]


class SetUsernameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "new_email", "re_new_email", "current_password"]
