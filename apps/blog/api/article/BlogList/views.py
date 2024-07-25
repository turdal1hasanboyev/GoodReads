from rest_framework.generics import ListAPIView

from apps.blog.models import Article
from apps.blog.api.article.BlogList.serializer import ArticleListSerializer


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    
    def get_queryset(self):
        return Article.objects.filter(is_active=True).select_related("category", "author").prefetch_related("tags")
    