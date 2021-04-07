from django.db import models

# Create your models here.
"""User account
login (email used for communication and notifications)
password
user name (presented on the account profile)
city
address (street, home number, ZIP code)2 | 5
account creation date
account status (ACTIVE / INACTIVE / BLOCKED)
logotype / thumbnail / avatar
type (NORMAL/PREMIUM)
"""
class User(models.Model):
    login = models.EmailField()
    password = models.CharField('password', max_length=128)
    user_name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=128)
    account_creation_date = models.DateTimeField(auto_now=True)
    account_status = models.CharField(default='ACTIVE', max_length=20)
    logotype = models.ImageField(upload_to='media/users/')
    type = models.CharField(default='NORMAL', max_length=20)

    def __str__(self):
        return self.login

class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

"""Auction details
title
description
photos (optional)
category
minimum to pay
Buy Now amount ( it disappears if the auction is started)
promoted (it can be assumed, that a premium account can promote e.g. 10 auctions a month)
location (corresponds to the location of the user account)
auction start date
auction end date
number of visits (page views)
"""

class Item(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    photos = models.ImageField(upload_to='media',blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    min_to_pay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    buy_now = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    promoted = models.BooleanField()
    location = models.CharField(max_length=60, default='Your city')
    auction_start_date = models.DateTimeField(auto_now=True)
    auction_end_date = models.DateTimeField()
    no_of_visits = models.IntegerField(editable=False, default=0)


    def __str__(self):
        return self.title + '-' + str(self.id)


"""Bidding
auction
user
amount to pay
"""
class Bidding(models.Model):
    auction = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2)
"""Purchase (the highest bid or Buy now)
auction
user
amount to pay
"""
class Purchase(models.Model):
    auction = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2)

"""Auction observation
auction
user
"""
class Watchlist(models.Model):
    auction = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
"""Transaction (purchase) assessment
purchase
seller rating
seller’s comment
buyer’s rating
buyer's comment
"""
class Transaction(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.DO_NOTHING)
    seller_rating = models.IntegerField()
    sellers_comment = models.TextField(max_length=250)
    buyer_rating = models.IntegerField()
    buyers_comment = models.TextField(max_length=250)