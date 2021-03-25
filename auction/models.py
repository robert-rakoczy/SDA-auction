from django.db import models

# Create your models here.

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
    #location = ??
    auction_start_date = models.DateTimeField(auto_now=True)
    auction_end_date = models.DateTimeField()
    #no_of_visits = models.


    def __str__(self):
        return self.title + '-' + str(self.id)