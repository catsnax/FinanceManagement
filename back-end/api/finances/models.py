from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        INCOME = 'IN', 'Income'
        EXPENSE = 'EX', 'Expense'
        INVESTMENT = 'IV', 'Investment'

    amount = models.DecimalField(decimal_places = 2, max_digits = 12)
    transaction_date = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    notes = models.TextField()
    transaction_type = models.CharField(max_length = 2, choices = TransactionType)

    class Meta:
        ordering = ['-transaction_date']
        indexes = [
            models.Index(fields = ['-transaction_date'])
            ]

    def __str__(self):
        return f"{self.transaction_type : self.amount}"

