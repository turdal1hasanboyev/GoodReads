from rest_framework.serializers import ModelSerializer

from apps.blog.models import Article


class ArticleCreateSerializer(ModelSerializer):
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
            "created_at",
        )

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
        