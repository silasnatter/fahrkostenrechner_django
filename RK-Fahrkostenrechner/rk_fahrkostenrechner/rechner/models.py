from django.db import models

# Create your models here.

class Kosten(models.Model):
    price = models.CharField(max_length=30,default=0,null=0)
    pauschal = models.CharField(max_length=30,default=0,null=0)

    def __str__(self):
        return "Bearbeiten"

class MapBox(models.Model):
    api_key = models.CharField(max_length=100)
    email = models.CharField(max_length=100,default=0,null=0)
    password = models.CharField(max_length=100,default=0,null=0)

    def __str__(self):
        return "Daten"