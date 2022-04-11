from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    account = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, default='from account_models')
