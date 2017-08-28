from __future__ import unicode_literals

from django.db import models
#from Products.models import Product
from Products.models import Design
from Products.models import Medium
design = models.ForeignKey(Design)
medium = models.ForeignKey(Medium)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True)
  #  products = models.ManyToManyField(Product, blank=True)
    designs = models.ManyToManyField(Design, blank=True)
    media = models.ManyToManyField(Medium, blank=True)

    def __str__(self):
        return self.name