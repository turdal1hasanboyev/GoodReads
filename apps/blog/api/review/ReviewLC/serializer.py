from rest_framework.serializers import ModelSerializer

from apps.blog.models import Review


class BlogReviewLCSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            "user",
            'article',
            "rate",
            'review',
            "created_at",
        )

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
        