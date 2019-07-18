from django.db import models

# Create your models here.

class Post(models.Model):
    number=models.IntegerField(unique=True)
    result = models.CharField(max_length=10000, default=None)
    # description = models.CharField(max_length=40, default=None)