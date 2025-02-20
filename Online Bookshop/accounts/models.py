from django.db import models
from django.contrib.auth.models import User
from book.models import Book
from accounts.constants import BADGES, BRONZE, SILVER, GOLD, DIAMOND, PLATINUM

class UserBookShopAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', primary_key=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    borrowed_books = models.ManyToManyField(Book, related_name='borrowed_books', blank=True)
    user_badge = models.IntegerField(choices=BADGES, default=BRONZE)
    coins = models.IntegerField(default=100)


    def save(self, *args, **kwargs):
        borrowed_books_count = self.borrowed_books.count() 
        if self.coins >= 1000 or borrowed_books_count >= 20:
            self.user_badge = PLATINUM
        elif self.coins >= 700 or borrowed_books_count >= 10:
            self.user_badge = DIAMOND
        elif self.coins >= 400 or borrowed_books_count >= 5:
            self.user_badge = GOLD
        elif self.coins >= 200 or borrowed_books_count >= 2:
            self.user_badge = SILVER
        else:
            self.user_badge = BRONZE

        super(UserBookShopAccount, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username}"


class DepositMoney(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deposit')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} deposited {self.amount} on {self.date}"
