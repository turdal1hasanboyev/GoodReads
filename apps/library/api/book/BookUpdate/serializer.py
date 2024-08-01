from rest_framework.serializers import ModelSerializer

from apps.library.models import Book
from apps.user.api.CustomUser.serializer import CustomUserSerializer


class BookUpdateSerializer(ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            "name",
            "slug",
            "author",
            "description",
            'published_at',
            "genres",
            "pages",
            "award",
            "cover",
            "created_at",
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
            "published_at": {"read_only": True},
            "created_at": {"read_only": True},
        }
        