from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Expense(models.Model):
    user_id = models.CharField(max_length=100, null=True)
    desc = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(null=False)
    time_stamp = models.DateTimeField(auto_now_add=True)


class Code(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)


class Feedback(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=300, null=True)
    created = models.DateTimeField(auto_now_add=True)
    