from rest_framework.generics import RetrieveAPIView

from apps.blog.models import Category
from apps.blog.api.category.CategoryDetail.serializer import CategoryRetrieveSerializer


class CategoryRetrieveView(RetrieveAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryRetrieveSerializer
    lookup_field = "slug"
    