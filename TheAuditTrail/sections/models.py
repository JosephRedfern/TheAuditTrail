from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Section(models.Model):
    index = models.IntegerField()
    region = models.ForeignKey('Region')

class Region(models.Model):
    name = models.CharField(max_length=255)
   
class Event(models.Model):
    name = models.CharField(max_length=255) 
    data = models.DateTimeField()

class Registration(models.Model):
    user = models.ForeignKey(User, unique=True)
    section = models.ForeignKey('Section')
    event = models.ForeignKey('Event')
