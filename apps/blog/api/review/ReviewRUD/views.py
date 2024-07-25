from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.blog.models import Review
from apps.blog.api.review.ReviewRUD.serializer import ReviewRUDSerializer


class ReviewRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewRUDSerializer
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_queryset(self):
        return Review.objects.filter(is_active=True).select_related("article", "user")
        