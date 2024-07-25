from rest_framework.serializers import ModelSerializer

from apps.blog.models import Article
from apps.user.api.CustomUser.serializer import CustomUserSerializer
from apps.blog.api.category.CategoryList.serializer import CategoryListSerializer
from apps.blog.api.tag.TagLC.serializer import TagLCSerializer


class ArticleListSerializer(ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    category = CategoryListSerializer(read_only=True)
    tags = TagLCSerializer(read_only=True, many=True)


    class Meta:
        model = Article
        fields = (
            'id',
            'slug',
            "name",
            "description",
            "image",
            "category",
            "tags",
            "author",
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
        }
        