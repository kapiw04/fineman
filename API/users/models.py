from django.db import models
from django.contrib.auth.models import User
# Omit creation of 'User' class since it's predefined in django

# Create your models here.

# Setting all on_delete as protect

class Account(models.Model):
    name = models.CharField(max_length=500)
    # One account can have many users
    # One user can have multiple accounts

    # By default, Django gives each model the following field:
    # id = models.AutoField(primary_key=True)

    users = models.ManyToManyField(User)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    name = models.CharField(max_length=500)
    # One transaction can have multiple accounts
    # One account can have multiple transactions
    accounts = models.ManyToManyField(Account)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=500)
    # There exist sub-categories
    # Product may not be of a certain sub-category
    subcategory = models.ForeignKey('self', null=True, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=500)
    # One transaction item can have one product
    # One product can have multiple transaction items

    # One product can have one category 
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class TransactionItem(models.Model):
    name = models.CharField(max_length=500)
    # One transaction item can have many transactions
    # One transaction can have many transaction items

    transactions = models.ManyToManyField(Account)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    def __str__(self):
        return self.name
