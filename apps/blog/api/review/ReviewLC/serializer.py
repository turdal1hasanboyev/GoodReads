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
        )

        extra_kwargs = {
            "id": {"read_only": True},
        }
        