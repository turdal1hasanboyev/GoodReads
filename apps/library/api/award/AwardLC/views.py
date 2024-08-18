from rest_framework.generics import ListCreateAPIView

from apps.library.models import Award
from .serializer import AwardLCSerializer


class AwardLCView(ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardLCSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(is_active=True).order_by("-date__year")
    