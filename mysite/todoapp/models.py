from django.db import models


# Create your models here.
class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
    title = models.CharField(max_length=20, default='')
    category = models.CharField(max_length=20, default='None')
