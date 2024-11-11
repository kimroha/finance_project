from django.db import models

# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),   
        ('withdrawal', 'Withdrawal'),  
        ('transfer', 'Transfer'),    
    ]

    TRANSACTION_METHODS = [
        ('cash', 'Cash'),   
        ('bank_transfer', 'Bank Transfer'),   
        ('card', 'Card'),    
        ('online', 'Online Payment'),  
    ]
    
    account_number = models.CharField(max_length=20)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    balance_after_transaction = models.DecimalField(max_digits=10, decimal_places=2)  
    transaction_detail = models.TextField()  
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)  
    transaction_method = models.CharField(max_length=20, choices=TRANSACTION_METHODS)  
    transaction_datetime = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} on {self.transaction_datetime}"

    class Meta:
        ordering = ['-transaction_datetime']  