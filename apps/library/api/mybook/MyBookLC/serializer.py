from rest_framework.serializers import ModelSerializer

from apps.library.models import MyBook
from apps.user.api.CustomUser.serializer import CustomUserSerializer
from apps.library.api.book.BookList.serializer import BookListSerializer


class MyBookLCSerializer(ModelSerializer):
    user = CustomUserSerializer
    book = BookListSerializer


    class Meta:
        model = MyBook
        fields = (
            'id',
            "user",
            'book',
            'date_read',
        )

        extra_kwargs = {
            "id": {"read_only": True},
        }
        