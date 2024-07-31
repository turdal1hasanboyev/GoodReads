from rest_framework.serializers import ModelSerializer

from apps.library.models import Book
from apps.user.api.CustomUser.serializer import CustomUserSerializer


class BookCreateSerializer(ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            "name",
            "slug",
            "description",
            'published_at',
            "genres",
            'author',
            "pages",
            "award",
            "cover",
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
        }
        