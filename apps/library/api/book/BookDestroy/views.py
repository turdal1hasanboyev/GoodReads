from rest_framework.generics import DestroyAPIView

from apps.library.models import Book
from apps.library.api.book.BookDestroy.serializer import BookDestroySerializer


class BookDestroyView(DestroyAPIView):
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookDestroySerializer
    lookup_field = "slug"

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
