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
from .models import  UserTokens
from pprint import pprint
import random
import string
from django.conf import settings

from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import uuid
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection, send_mail
from django.contrib.auth import get_user_model

# https://stackoverflow.com/questions/2809547/creating-email-templates-with-django

class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "username",
        ]


class UserSerializer(UserSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
        ]





class SendEmailResetSerializer(ModelSerializer):
    parthner = serializers.CharField()
    class Meta:
        model = UserTokens
        fields = [ "email", "parthner"]


    def validate_parthner(self, parthner):
        # pprint(parthner)
        parthner = parthner.upper()
        if parthner not in settings.WEBSITES:
            raise serializers.ValidationError("Parthner not found")
            
        return parthner
    def validate_email(self, email):
        UserTokens.objects.filter(email=email).delete()
        # pprint(email)
        # email = email.upper()
        # if email not in settings.WEBSITES:
        #     raise serializers.ValidationError("Pathner not found")
            
        return email
        
    
    
    def create(self, validated_data):
        User = get_user_model()
        email = validated_data['email']
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email not found")

        UserTokens.objects.filter(email=email).delete()
        reset_instance = UserTokens.objects.create(email=email, token=uuid.uuid4())

        parthner = validated_data['parthner']
        convert_to_html_content =  render_to_string(
                                    template_name='emails/email_restore.html',
                                    context={'username': email,'token': reset_instance.token, 'parthner':parthner
                                             , 'website':f"{settings.EMAILS[validated_data['parthner']]['WEBSITE']}/reset/uid/{reset_instance.token}/"
                                             , 'logo':f"{settings.EMAILS[validated_data['parthner']]['LOGO']}"
                                              }
                                    )
        plain_message = strip_tags(convert_to_html_content) 



        connection = get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAILS[validated_data['parthner']]['EMAIL'],
            password=settings.EMAILS[validated_data['parthner']]['PASSWORD'],
            use_tls=settings.EMAIL_USE_TLS)

        


        # Send an email using the custom connection
        send_mail(
            # 'Subject',
            #        msg_plain,settings.EMAILS[validated_data['parthner']]['EMAIL'], 
            #        [email],
            #        html_message=msg_html,  
            #     #    context={'username': 'John'},
                  
            #       connection=connection
                  
                  
                            
            subject="Restaurar a conta",
            message=plain_message,
            from_email=settings.EMAILS[validated_data['parthner']]['EMAIL'],
            recipient_list=[email],  
            html_message=convert_to_html_content,
            fail_silently=True,   # Optional

                  connection=connection

                  
                  )
      

        return validated_data

class PasswordResetConfirmRetypeSerializer(ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ["id", "uid", "token", "new_password", "re_new_password"]

    def create(self, validated_data):
        email = validated_data['email']
        UserTokens.objects.filter(email=email).delete()
        reset_instance = UserTokens.objects.create(email=email)

        return reset_instance


class SetPasswordRetypeSerializer(ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ["id", "current_password", "new_password", "re_new_password"]


class SetUsernameSerializer(ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ["id", "new_email", "re_new_email", "current_password"]
