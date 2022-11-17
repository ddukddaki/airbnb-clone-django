from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Experience
from .models import Perk
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from wishlists.models import Wishlist


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

    host = TinyUserSerializer(
        read_only=True,
    )
    category = CategorySerializer(
        read_only=True,
    )
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()
    is_liked = SerializerMethodField()

    class Meta:
        model = Experience
        exclude = ("perks",)

    def get_rating(self, experience):
        return experience.rating()

    def get_is_owner(self, experience):
        request = self.context["request"]
        return experience.host == request.user

    def get_is_liked(self, experience):
        request = self.context["request"]
        return Wishlist.objects.filter(user=request.user, experiences__pk=experience.pk).exists()
