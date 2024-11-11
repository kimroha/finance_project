from django.db import models
from django.conf import settings

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 사용자
    account_number = models.CharField(max_length=100, unique=True)  # 계좌번호
    bank_code = models.CharField(max_length=10)  # 은행코드
    transaction_type = models.CharField(max_length=20)  # 거래 타입
    balance = models.DecimalField(max_digits=15, decimal_places=2)  # 잔고

    def __str__(self):
        return f"Account {self.account_number} - User: {self.user.email}"