from rest_framework.generics import CreateAPIView

from apps.blog.models import Article
from .serializer import ArticleCreateSerializer


class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    