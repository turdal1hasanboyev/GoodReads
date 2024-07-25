from rest_framework.serializers import ModelSerializer

from apps.library.models import Book
from apps.user.api.CustomUser.serializer import CustomUserSerializer


class BookListSerializer(ModelSerializer):
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
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
        }
        