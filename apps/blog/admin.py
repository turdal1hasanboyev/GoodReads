from django.contrib import admin

from apps.blog.models import Category, Tag, Article, Review


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Review)
