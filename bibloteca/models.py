from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Statu(models.Model):
    descriptions = models.CharField(max_length = 100)

    def __str__(self):
        return self.descriptions
    
class Book(models.Model):
    title = models.CharField(max_length = 300)
    author = models.CharField(max_length = 300)
    numPages = models.IntegerField()
    statu = models.ForeignKey(Statu , on_delete=models.CASCADE)
    currentPage = models.IntegerField(default = 0)
    image = models.CharField(max_length = 300 ,default = '' )

class Library(models.Model):
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

