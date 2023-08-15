from djoser.serializers import (
    UserCreateSerializer,
    UserSerializer,
    SetPasswordRetypeSerializer,
    SetUsernameSerializer,
    SendEmailResetSerializer,
    PasswordResetConfirmRetypeSerializer,
)
from django.db.transaction import atomic

from .models import User
from pprint import pprint


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "code",
            "phone",
            "email",
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
            "phone",
            "code",
        ]


class SendEmailResetSerializer(SendEmailResetSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]


class PasswordResetConfirmRetypeSerializer(PasswordResetConfirmRetypeSerializer):
    class Meta:
        model = User
        fields = ["id", "uid", "token", "new_password", "re_new_password"]


class SetPasswordRetypeSerializer(SetPasswordRetypeSerializer):
    class Meta:
        model = User
        fields = ["id", "current_password", "new_password", "re_new_password"]


class SetUsernameSerializer(SetUsernameSerializer):
    class Meta:
        model = User
        fields = ["id", "new_email", "re_new_email", "current_password"]


class SetUsernameSerializer(SetUsernameSerializer):
    class Meta:
        model = User
        fields = ["id", "new_email", "re_new_email", "current_password"]

    # atomic()

    # def update(self, instance, validated_data):
    #     pprint(validated_data)
    #     data = validated_data
    #     data['email'] = data['new_username']
    #     return super().update(instance, data)


# new_password
# re_new_password
# current_password
# HTTP 204 No Content

# new_{USERNAME_FIELD}
# re_new_{USERNAME_FIELD}
# current_password
