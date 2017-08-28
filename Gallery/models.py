from  __future__ import unicode_literals
from django.db import models

# Create your models here.

class Gallery(models.Model):
        name = models.CharField(max_length=254, default='')
        description = models.TextField()
        price = models.DecimalField(max_digits=9, decimal_places=2)
        image = models.ImageField(upload_to='Static/Images')

        def __str__(self):
            return self.name

