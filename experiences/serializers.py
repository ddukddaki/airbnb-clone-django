from rest_framework.serializers import ModelSerializer
from .models import Experience
from .models import Perk
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceListSerializer(ModelSerializer):

    host = TinyUserSerializer(
        read_only=True,
    )
    category = CategorySerializer(
        read_only=True,
    )

    class Meta:
        model = Experience
        exclude = (
            "id",
            "created_at",
            "updated_at",
            "perks",
        )


class ExperienceDetailSerializer(ModelSerializer):
    class Meta:
        model = Experience
        exclude = ("perks",)
