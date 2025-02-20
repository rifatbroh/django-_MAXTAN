from django.db import models
from review.models import Review
from django.utils.text import slugify

class Book(models.Model):
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE, related_name='books_by_author')
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='books/', blank=True, null=True, default='b1.jpg')
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)  
    price = models.DecimalField(max_digits=12, decimal_places=2)
    price_with_coin = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    reviews = models.ManyToManyField(Review, related_name='book_reviews', blank=True)
    categories = models.ManyToManyField('Category', related_name='books', blank=True)
    borrow_count = models.PositiveIntegerField(default=0) 
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ('-added',)

    def save(self, *args, **kwargs):
        if not self.price_with_coin:
            coin_conversion_rate = 13
            self.price_with_coin = self.price * coin_conversion_rate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
