from django.urls import path

from apps.library.api.genre.GenreLC.views import GenreLCView
from apps.library.api.genre.GenreRUD.views import GenreRUDView

from apps.library.api.award.AwardLC.views import AwardLCView
from apps.library.api.award.AwardRUD.views import AwardRUDView

from apps.library.api.mybook.MyBookLC.views import MyBookLCView
from apps.library.api.mybook.MyBookRUD.views import MyBookRUDView

from apps.library.api.book.BookList.views import BookListView
from apps.library.api.book.BookCreate.views import BookCreateView
from apps.library.api.book.BookDestroy.views import BookDestroyView
from apps.library.api.book.BookDetail.views import BookRetrieveView
from apps.library.api.book.BookUpdate.views import BookUpdateView

from apps.library.api.review.ReviewLC.views import ReviewLCView
from apps.library.api.review.ReviewRUD.views import ReviewRUDView


app_name = "library"


urlpatterns = [
    path('genrelc/', GenreLCView.as_view(), name='genre_lc'),
    path('genrerud/<int:pk>/', GenreRUDView.as_view(), name='genre_rud'),

    path("awardlc/", AwardLCView.as_view(), name="award_lc"),
    path("awardrud/<int:pk>/", AwardRUDView.as_view(), name="award_rud"),

    path("mybooklc/", MyBookLCView.as_view(), name="mybook_lc"),
    path("mybookrud/<int:pk>/", MyBookRUDView.as_view(), name="mybook_rud"),

    path('booklist/', BookListView.as_view(), name="book_list"),
    path('bookcreate/', BookCreateView.as_view(), name="book_create"),
    path('bookdelete/<slug:slug>/', BookDestroyView.as_view(), name="book_destroy"),
    path('bookdetail/<slug:slug>/', BookRetrieveView.as_view(), name="book_detail"),
    path('bookupdate/<slug:slug>/', BookUpdateView.as_view(), name="book_update"),

    path("reviewlc/", ReviewLCView.as_view(), name="review_lc"),
    path("reviewrud/<int:pk>/", ReviewRUDView.as_view(), name="review_rud"),
]
