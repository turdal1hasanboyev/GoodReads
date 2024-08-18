from rest_framework.generics import ListCreateAPIView

from apps.blog.models import Tag
from .serializer import TagLCSerializer


class TagLCView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    