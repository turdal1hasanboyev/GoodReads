from rest_framework.serializers import ModelSerializer

from apps.library.models import Book
from apps.user.api.CustomUser.serializer import CustomUserSerializer
from apps.library.api.award.AwardLC.serializer import AwardLCSerializer
from apps.library.api.genre.GenreLC.serializer import GenreLCSerializer


class BookListSerializer(ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    award = AwardLCSerializer(many=True)
    genres  = GenreLCSerializer(many=True)

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
        