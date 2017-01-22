from __future__ import unicode_literals

from django.db import models

# class Item(models.Model):
#     """docstring for Item."""
#     def __init__(self, arg):
#         super(Item, self).__init__()
#         self.arg = arg
#

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=2,max_digits=12)
