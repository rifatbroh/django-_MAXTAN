from django.urls import path
from book.views import BookDetailsView, BorrowBookWithMoney, BorrowBookWithCoins, ReturnBook

urlpatterns = [
    path('book/<int:pk>/', BookDetailsView.as_view(), name='book_details'),
    path('borrow-with-money/<int:pk>/', BorrowBookWithMoney.as_view(), name='borrow_with_money'),
    path('borrow-with-coins/<int:pk>/', BorrowBookWithCoins.as_view(), name='borrow_with_coins'),
    path('return/<int:pk>/', ReturnBook.as_view(), name='return_book'),
]

