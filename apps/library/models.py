from django.db import models

import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"


class Award(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"


class Book(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=225, db_index=True, null=True, blank=True)
    author = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="books",
        limit_choices_to={"is_author": True},
    )
    description = RichTextField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    published_at = models.DateField(null=True, blank=True)
    pages = models.IntegerField(default=0, null=True, blank=True)
    award = models.ManyToManyField(Award, blank=True)
    cover = models.ImageField(upload_to="Covers/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)
    

class Review(BaseModel):
    STATUS = (
        (0, _("read")),
        (1, _("currently-reading")),
        (2, _("to-read"))
    )
    author = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="reviews",
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True, related_name="book_reviews")
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    bookshelve = models.IntegerField(default=None, choices=STATUS, null=True, blank=True)
    date_started = models.DateField(null=True, blank=True)
    date_ended = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.author.get_full_name()} - {self.book}"


class MyBook(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True, blank=True, related_name="my_books")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True, related_name="favorites")
    date_read = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.user.get_full_name()} - {self.book}"
    

class FriendRequest(BaseModel):
    from_user = models.ForeignKey(
        "user.User",
        related_name='from_users',
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    to_user = models.ForeignKey(
        "user.User",
        related_name='to_users',
        on_delete=models.CASCADE,
        null=True, blank=True,
    )

    def __str__(self):
        return f"{self.id} - {self.from_user} to {self.to_user}"
    