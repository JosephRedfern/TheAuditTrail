from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Section(models.Model):
    index = models.IntegerField()
    region = models.ForeignKey('Region')

    def __unicode__(self):
        return "Section %d" % (self.index)

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
   
class Event(models.Model):
    name = models.CharField(max_length=255) 
    date = models.DateTimeField()

    def __unicode__(self):
        return "Event %s on %s" % (self.name, self.date)

class Registration(models.Model):
    user = models.ForeignKey(User, unique=True)
    section = models.ForeignKey('Section')
    event = models.ForeignKey('Event')

    def __unicode__(self):
        return "Registration by %s for %s" % (self.user, self.event)
