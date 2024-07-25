from rest_framework.serializers import ModelSerializer

from apps.blog.models import Review
from apps.user.api.CustomUser.serializer import CustomUserSerializer


class ReviewLCSerializer(ModelSerializer):
    user = CustomUserSerializer


    class Meta:
        model = Review
        fields = (
            'id',
            "user",
            'article',
            "rate",
            'review',
        )

        extra_kwargs = {
            "id": {"read_only": True},
        }
        