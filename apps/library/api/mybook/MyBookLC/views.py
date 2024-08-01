from rest_framework.generics import ListCreateAPIView

from apps.library.models import MyBook
from apps.library.api.mybook.MyBookLC.serializer import MyBookLCSerializer
from apps.common.permissions import IsAuthor


class MyBookLCView(ListCreateAPIView):
    queryset = MyBook.objects.all()
    serializer_class = MyBookLCSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("user", "book")
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    