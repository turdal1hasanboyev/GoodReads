from rest_framework.serializers import ModelSerializer

from apps.library.models import MyBook
from apps.user.api.CustomUser.serializer import CustomUserSerializer


class MyBookRUDSerializer(ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = MyBook
        fields = (
            'id',
            "user",
            'book',
            'date_read',
            "created_at",
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
        