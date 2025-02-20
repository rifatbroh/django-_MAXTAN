from django.db import models
from django.contrib.auth.models import User
from review.constants import RATINGS

class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    book = models.ForeignKey('book.Book', related_name='reviewed_books', on_delete=models.CASCADE) 
    ratings = models.PositiveSmallIntegerField(choices=RATINGS) 
    description = models.TextField(null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title}"
