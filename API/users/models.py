from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    # account_set added implicitly
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

class Category(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class ProductGroup(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    accounts = models.ManyToManyField(Account)

class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(ProductGroup, on_delete = models.CASCADE)

class TransactionItem(models.Model):
    quantity = models.FloatField()
    price = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)


