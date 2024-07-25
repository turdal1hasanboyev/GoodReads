from rest_framework.serializers import ModelSerializer

from apps.blog.models import Category


class CategoryDestroySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            "name",
            "slug",
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
        }
        