from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True)  # 아이디
    email = models.CharField(max_length=255, unique=True)  # 이메일
    name = models.CharField(max_length=100)  # 이름
    nickname = models.CharField(max_length=100, unique=True)  # 닉네임
    password = models.CharField(max_length=255)  # 비밀번호
    phone_number = models.CharField(max_length=20)  # 휴대폰번호

    def __str__(self):
        return self.nickname