from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import Transaction

class TransactionView(LoginRequiredMixin, View):
    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        return render(request, 'transactions/transaction_report.html', {'transactions' : transactions})
