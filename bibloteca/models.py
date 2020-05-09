from django.db import models

class Statu(models.Model):
    descriptions = models.CharField(max_length = 100)

    def __str__(self):
        return self.descriptions
    