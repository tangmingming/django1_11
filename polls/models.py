from django.db import models

# Create your models here.

class Question(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Q_item(models.Model):
    question = models.ForeignKey(Question)
    name = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        self.name