from rest_framework.serializers import ModelSerializer

from apps.blog.models import Tag


class TagRUDSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
            "slug",
            "created_at",
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
        