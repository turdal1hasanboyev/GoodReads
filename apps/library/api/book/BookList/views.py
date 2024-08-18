from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.library.models import Book
from .serializer import BookListSerializer
from .filter import BookFilter

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("author").prefetch_related("award", "genres")
    