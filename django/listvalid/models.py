from django.db import models

class List(models.Model):
    list = models.CharField(max_length = 100)