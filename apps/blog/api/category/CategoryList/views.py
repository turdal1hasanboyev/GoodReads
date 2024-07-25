from rest_framework.generics import ListAPIView

from apps.blog.models import Category
from apps.blog.api.category.CategoryList.serializer import CategoryListSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    