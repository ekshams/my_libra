from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=32)
    author_name = models.CharField(max_length=32)
    subject = models.ForeignKey(Subject)
    price = models.IntegerField()
    book_image = models.FileField()


    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name
