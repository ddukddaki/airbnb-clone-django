from rest_framework.serializers import ModelSerializer
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )


class ManageBookingTinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "phone_nb",
        )


class UserSignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "phone_nb",
            "email",
            "username",
        )


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )
