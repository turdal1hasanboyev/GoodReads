from django.urls import path

from apps.blog.api.article.BlogCreate.views import ArticleCreateView
from apps.blog.api.article.BlogList.views import ArticleListView
from apps.blog.api.article.BlogRUD.views import ArticleRUDView

from apps.blog.api.category.CategoryCreate.views import CategoryCreateView
from apps.blog.api.category.CategoryDestroy.views import CategoryDestroyView
from apps.blog.api.category.CategoryDetail.views import CategoryRetrieveView
from apps.blog.api.category.CategoryList.views import CategoryListView
from apps.blog.api.category.CategoryUpdate.views import CategoryUpdateView

from apps.blog.api.tag.TagLC.views import TagLCView
from apps.blog.api.tag.TagRUD.views import TagRUDView

from apps.blog.api.review.ReviewLC.views import ReviewLCView
from apps.blog.api.review.ReviewRUD.views import ReviewRUDView


app_name = "blog"

urlpatterns = [
    path('articlecreate/', ArticleCreateView.as_view(), name="article_create"),
    path('articlelist/', ArticleListView.as_view(), name="article_list"),
    path('articlerud/<slug:slug>/', ArticleRUDView.as_view(), name="article_rud"),

    path('categorycreate/', CategoryCreateView.as_view(), name="category_create"),
    path('categorylist/', CategoryListView.as_view(), name="category_list"),
    path('categoryupdate/<slug:slug>/', CategoryUpdateView.as_view(), name="category_edit"),
    path('categorydetail/<slug:slug>/', CategoryRetrieveView.as_view(), name="category_detail"),
    path('categorydelete/<slug:slug>/', CategoryDestroyView.as_view(), name="category_delete"),

    path('taglc/', TagLCView.as_view(), name="tag_lc"),
    path('tagrud/<slug:slug>/', TagRUDView.as_view(), name="tag_rud"),

    path('reviewlc/', ReviewLCView.as_view(), name="review_lc"),
    path('reviewrud/<int:pk>/', ReviewRUDView.as_view(), name="review")
]
