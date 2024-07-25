from rest_framework.serializers import ModelSerializer

from apps.library.models import Review
from apps.user.api.CustomUser.serializer import CustomUserSerializer
from apps.library.api.book.BookList.serializer import BookListSerializer


class ReviewRUDSerializer(ModelSerializer):
    author = CustomUserSerializer
    book = BookListSerializer


    class Meta:
        model = Review
        fields = (
            'id',
            'author',
            "book",
            "rate",
            "review",
            "bookshelve",
            "date_started",
            "date_ended",
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
        }
        