from django.db import models

# Create your models here.

class Table (models.Model):
    resource = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
