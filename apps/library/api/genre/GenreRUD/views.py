from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.library.models import Genre
from .serializer import GenreRUDSerializer


class GenreRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreRUDSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("parent")
        