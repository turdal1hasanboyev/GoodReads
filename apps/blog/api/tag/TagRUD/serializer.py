from rest_framework.serializers import ModelSerializer

from apps.blog.models import Tag


class TagRUDSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
            "slug",
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
        }
        