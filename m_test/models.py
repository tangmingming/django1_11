from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=20)
    state_province = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.SmallIntegerField()
    authors = models.ManyToManyField("Author")
    publish = models.ForeignKey("Publisher")
    publish_date = models.DateField()
