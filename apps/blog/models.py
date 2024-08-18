from django.db import models

from ckeditor.fields import RichTextField

from django.template.defaultfilters import slugify

from django.core.validators import MinValueValidator, MaxValueValidator

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.id} - {self.name}"
    

class Tag(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Article(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='Blogs/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="articles")
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.id} - {self.name}"


class Review(BaseModel):
    user = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="article_reviews",
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name="article_reviews")
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.article}"
    