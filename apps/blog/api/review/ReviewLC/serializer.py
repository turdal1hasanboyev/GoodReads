from rest_framework.serializers import ModelSerializer

from apps.blog.models import Review
from apps.user.api.CustomUser.serializer import CustomUserSerializer
from apps.blog.api.article.BlogList.serializer import ArticleListSerializer


class BlogReviewLCSerializer(ModelSerializer):
    user = CustomUserSerializer
    article = ArticleListSerializer

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
        