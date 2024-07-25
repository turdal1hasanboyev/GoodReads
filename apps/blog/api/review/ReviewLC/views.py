from rest_framework.generics import ListCreateAPIView

from apps.blog.models import Review
from apps.blog.api.review.ReviewLC.serializer import ReviewLCSerializer


class ReviewLCView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    