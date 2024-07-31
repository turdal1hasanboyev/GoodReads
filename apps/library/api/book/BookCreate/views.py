from rest_framework.generics import CreateAPIView

from apps.library.models import Book
from apps.library.api.book.BookCreate.serializer import BookCreateSerializer
from apps.common.permissions import IsAuthor


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = [IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    