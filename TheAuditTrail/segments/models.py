from django.db import models

# Create your models here.

class Section(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=255)
    region = models.ForeignKey('Region')

class Region(models.Model):
    name = models.CharField(max_length=255)
