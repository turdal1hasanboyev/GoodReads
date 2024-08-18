from django.contrib import admin

from .models import Genre, Award, Book, Review, MyBook, FriendRequest


admin.site.register(Genre)
admin.site.register(Award)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(MyBook)
admin.site.register(FriendRequest)
