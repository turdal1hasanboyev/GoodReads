from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.library.models import Award
from .serializer import AwardRUDSerializer


class AwardRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardRUDSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()

    def get_queryset(self):
        return Award.objects.filter(is_active=True)
        