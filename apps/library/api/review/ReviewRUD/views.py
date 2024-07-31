from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.library.models import Review
from apps.library.api.review.ReviewRUD.serializer import ReviewRUDSerializer


class ReviewRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewRUDSerializer
    lookup_field = "pk"
    
    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("author", "book")
        