from django.urls import path
from transactions.views import TransactionView

urlpatterns = [
    path('report/', TransactionView.as_view(), name='transaction_report'),
]

