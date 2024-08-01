from rest_framework.generics import UpdateAPIView

from apps.library.models import Book
from apps.library.api.book.BookUpdate.serializer import BookUpdateSerializer
from apps.common.permissions import IsAuthor


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookUpdateSerializer
    permission_clas = [IsAuthor]
    lookup_field = 'slug'
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    