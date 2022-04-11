from django.contrib.auth.models import User
from django.db import models

from account.models import Account
from products.models import Product


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Product)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)


class DateOrder(models.Model):
    create_time = models.DateTimeField()


class FamilyProfiles(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    DateOfBirthday = models.DateField()
