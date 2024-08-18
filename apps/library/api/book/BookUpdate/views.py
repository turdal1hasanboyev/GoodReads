from rest_framework.generics import UpdateAPIView

from apps.common.permissions import IsAuthor
from apps.library.models import Book
from .serializer import BookUpdateSerializer


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthor]
