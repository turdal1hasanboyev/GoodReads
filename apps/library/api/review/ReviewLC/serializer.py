from rest_framework.serializers import ModelSerializer

from apps.library.models import Review


class ReviewLCSerializer(ModelSerializer):
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
            "created_at",
        )

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
        