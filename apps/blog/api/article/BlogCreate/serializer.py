from rest_framework.serializers import ModelSerializer

from apps.blog.models import Article
from apps.user.api.CustomUser.serializer import CustomUserSerializer


class ArticleCreateSerializer(ModelSerializer):
    author = CustomUserSerializer

    
    class Meta:
        model = Article
        fields = (
            'id',
            "slug",
            "name",
            "description",
            "image",
            "category",
            "tags",
            "author",
        )

        extra_kwargs = {
            "id": {"read_only": True},
        }
        