from django.db import models
from django.contrib.auth.models import User
from transactions.constants import TRAX_TYPE


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction', null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    trax_type = models.CharField(choices=TRAX_TYPE, max_length=20)
    action = models.CharField(max_length=100, null=True, blank=True)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp'] 


    