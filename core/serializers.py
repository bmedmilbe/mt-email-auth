from pprint import pprint

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from djoser.serializers import (
    PasswordResetConfirmRetypeSerializer,
    SetPasswordRetypeSerializer,
    SetUsernameSerializer,
    UserCreateSerializer,
    UserSerializer,
)
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'phone', 'password', 'tenant', 'partner')
        validators = []

    def validate(self, attrs):
        # 1. Extract values from the data
        email = attrs.get('email')
        username = phone = attrs.get('phone')
        tenant = attrs.get('tenant')
        
        if phone == '':
            attrs['phone'] = None
            phone=None

        if email == '':
            attrs['email'] = None
            email = None
        else:
            username = email

        # 2. Logic: Require at least one (as requested previously)
        if not email and not phone:
            raise serializers.ValidationError(
                {"username": ["You must provide either an email or a phone number."]}
            )

        # 3. Validate duplicated Email per Tenant
        if email:
            if User.objects.filter(email=email, tenant=tenant).exists():
                raise serializers.ValidationError(
                    {"email": ["An user with this email already exists in this tenant."]}
                )

        # 4. Validate duplicated Phone per Tenant
        if phone:
            if User.objects.filter(phone=phone, tenant=tenant).exists():
                raise serializers.ValidationError(
                    {"phone": ["An user with this phone number already exists in this tenant."]}
                )

        attrs['username'] = f"{tenant.id}_{username}"

        return super().validate(attrs)
    


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



class TenantTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['tenant_id'] = user.tenant_id 
        return token