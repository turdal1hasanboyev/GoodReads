from rest_framework.generics import CreateAPIView

from apps.blog.models import Article
from apps.blog.api.article.BlogCreate.serializer import ArticleCreateSerializer


class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    