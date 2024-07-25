from rest_framework.generics import ListCreateAPIView

from apps.library.models import MyBook
from apps.library.api.mybook.MyBookLC.serializer import MyBookLCSerializer


class MyBookLCView(ListCreateAPIView):
    queryset = MyBook.objects.all()
    serializer_class = MyBookLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("user", "book")
    