from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from .models import Experience
from .serializers import ExperienceListSerializer, ExperienceDetailSerializer
from categories.models import Category


class Experiences(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        experiences = Experience.objects.all()
        serializer = ExperienceListSerializer(
            experiences,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperienceDetailSerializer(request.data)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required.")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoices.ROOMS:
                    raise ParseError("Category Kind should be rooms.")
            except Category.DoesNotExist:
                raise ParseError("Category Not Found.")
