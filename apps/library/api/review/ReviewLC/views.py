from rest_framework.generics import ListCreateAPIView

from apps.library.models import Review
from .serializer import ReviewLCSerializer


class ReviewLCView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("author", "book")
    