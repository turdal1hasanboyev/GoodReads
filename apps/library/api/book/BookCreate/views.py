from rest_framework.generics import CreateAPIView

from apps.library.models import Book
from apps.library.api.book.BookCreate.serializer import BookCreateSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    