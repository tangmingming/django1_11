from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.SmallIntegerField()
    authors = models.CharField(max_length=30)
