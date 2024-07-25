from rest_framework.serializers import ModelSerializer

from apps.blog.models import Tag


class TagLCSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'slug',
            "name",
        )

        extra_kwargs = {
            "id": {"read_only": True},
        }
        