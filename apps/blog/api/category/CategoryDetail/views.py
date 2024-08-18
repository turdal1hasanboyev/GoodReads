from rest_framework.generics import RetrieveAPIView

from apps.blog.models import Category
from .serializer import CategoryRetrieveSerializer


class CategoryRetrieveView(RetrieveAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryRetrieveSerializer
    lookup_field = "slug"
    