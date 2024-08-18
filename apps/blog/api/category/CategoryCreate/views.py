from rest_framework.generics import CreateAPIView

from apps.blog.models import Category
from .serializer import CategoryCreateSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    