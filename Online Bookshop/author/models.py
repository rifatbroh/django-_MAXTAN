from django.db import models
from book.models import Book

class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='author_images/', null=True, blank=True)
    address = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    books = models.ManyToManyField(Book, related_name='authors', blank=True)
    total_borrowed = models.IntegerField(null=True, blank=True, default=0)
    rank = models.IntegerField(null=True, blank=True)
    popularity = models.DecimalField(null=True, blank=True, default=0, decimal_places=2, max_digits=12)

    def __str__(self):
        return f"{self.name}"
    