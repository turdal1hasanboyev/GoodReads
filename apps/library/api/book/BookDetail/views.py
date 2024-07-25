from rest_framework.generics import RetrieveAPIView

from apps.library.models import Book
from apps.library.api.book.BookDetail.serializer import BookRetrieveSerializer


class BookRetrieveView(RetrieveAPIView):
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookRetrieveSerializer
    lookup_field = "slug"
    