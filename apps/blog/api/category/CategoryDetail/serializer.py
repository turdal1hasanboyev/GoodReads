from rest_framework.serializers import ModelSerializer

from apps.blog.models import Category


class CategoryRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            "name",
            "slug",
        )
        