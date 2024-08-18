from django.urls import path

from .api.article.BlogCreate.views import ArticleCreateView
from .api.article.BlogList.views import ArticleListView
from .api.article.BlogRUD.views import ArticleRUDView

from .api.category.CategoryCreate.views import CategoryCreateView
from .api.category.CategoryDestroy.views import CategoryDestroyView
from .api.category.CategoryDetail.views import CategoryRetrieveView
from .api.category.CategoryList.views import CategoryListView
from .api.category.CategoryUpdate.views import CategoryUpdateView

from .api.tag.TagLC.views import TagLCView
from .api.tag.TagRUD.views import TagRUDView

from .api.review.ReviewLC.views import ReviewLCView
from .api.review.ReviewRUD.views import ReviewRUDView


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
