from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.blog.models import Article
from apps.blog.api.article.BlogRUD.serializer import ArticleRUDSerializer


class ArticleRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleRUDSerializer
    lookup_field = "slug"
    
    def get_queryset(self):
        return Article.objects.filter(is_active=True).select_related("category", "author").prefetch_related("tags")
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
