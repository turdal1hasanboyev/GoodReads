from rest_framework.serializers import ModelSerializer

from apps.library.models import Book
from apps.user.api.CustomUser.serializer import CustomUserSerializer
from apps.library.api.award.AwardLC.serializer import AwardLCSerializer
from apps.library.api.genre.GenreLC.serializer import GenreLCSerializer


class BookUpdateSerializer(ModelSerializer):
    author = CustomUserSerializer
    genre = GenreLCSerializer
    award = AwardLCSerializer

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
        