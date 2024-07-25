from rest_framework.generics import ListCreateAPIView

from apps.library.models import Genre
from apps.library.api.genre.GenreLC.serializer import GenreLCSerializer


class GenreLCView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("parent")
    