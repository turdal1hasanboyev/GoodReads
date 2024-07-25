from rest_framework.generics import ListAPIView

from apps.library.models import Book
from apps.library.api.book.BookList.serializer import BookListSerializer

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("author").prefetch_related("award", "genres")
    