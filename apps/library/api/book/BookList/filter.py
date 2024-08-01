import django_filters as filters

from apps.library.models import Book


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='author__first_name__icontains')
    genres = filters.NumberFilter(lookup_expr='id__iexact')
    award = filters.NumberFilter(lookup_expr='id__iexact')
    published_at = filters.DateTimeFilter(field_name="published_at", lookup_expr='iexact')
    pages__gt = filters.NumberFilter(field_name="pages__gt", lookup_expr='gt')
    pages = filters.NumberFilter(field_name="pages", lookup_expr='iexact')

    class Meta:
        model = Book
        fields = [
            'name',
            'author',
            'genres',
            'award',
            'published_at',
            'pages__gt',
            'pages',
        ]
