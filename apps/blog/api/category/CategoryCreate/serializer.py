from rest_framework.serializers import ModelSerializer

from apps.blog.models import Category


class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            "name",
            "slug",
            "created_at",
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
        