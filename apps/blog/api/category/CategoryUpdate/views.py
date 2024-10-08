from rest_framework.generics import UpdateAPIView

from apps.blog.models import Category
from .serializer import CategoryUpdateSerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryUpdateSerializer
    lookup_field = 'slug'
    