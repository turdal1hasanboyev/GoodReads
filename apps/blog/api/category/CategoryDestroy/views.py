from rest_framework.generics import DestroyAPIView

from apps.blog.models import Category
from apps.blog.api.category.CategoryDestroy.serializer import CategoryDestroySerializer


class CategoryDestroyView(DestroyAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryDestroySerializer
    lookup_field = "slug"

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
