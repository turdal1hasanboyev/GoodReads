from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.library.models import MyBook
from apps.library.api.mybook.MyBookRUD.serializer import MyBookRUDSerializer
from apps.common.permissions import IsAuthor


class MyBookRUDView(RetrieveUpdateDestroyAPIView):
    queryset = MyBook.objects.all()
    serializer_class = MyBookRUDSerializer
    lookup_field = "pk"
    permission_classes = [IsAuthor]
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()

    def get_queryset(self):
        return MyBook.objects.filter(is_active=True).select_related("user", "book") 
    