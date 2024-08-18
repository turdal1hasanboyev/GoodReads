from django.urls import path

from .api.genre.GenreLC.views import GenreLCView
from .api.genre.GenreRUD.views import GenreRUDView

from .api.award.AwardLC.views import AwardLCView
from .api.award.AwardRUD.views import AwardRUDView

from .api.mybook.MyBookLC.views import MyBookLCView
from .api.mybook.MyBookRUD.views import MyBookRUDView

from .api.book.BookList.views import BookListView
from .api.book.BookCreate.views import BookCreateView
from .api.book.BookDestroy.views import BookDestroyView
from .api.book.BookDetail.views import BookRetrieveView
from .api.book.BookUpdate.views import BookUpdateView

from .api.review.ReviewLC.views import ReviewLCView
from .api.review.ReviewRUD.views import ReviewRUDView

from .api.friendrequest.FriendRequestCreate.views import FriendRequestCreateView
from .api.friendrequest.FriendRequestDestroy.views import FriendRequestDestroyView
from .api.friendrequest.FriendRequestRetrieve.views import MyFriendsView


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

    path("friendrequestcreate/", FriendRequestCreateView.as_view(), name="friend_request_create"),
    path("myfriends/", MyFriendsView.as_view(), name="my_friends"),
    path("unfollowfriend/<int:pk>/", FriendRequestDestroyView.as_view(), name="unfollow_friend")
]
