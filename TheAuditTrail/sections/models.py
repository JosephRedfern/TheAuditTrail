from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models

# Create your models here.

class Section(models.Model):
    index = models.IntegerField()
    region = models.ForeignKey('Region')
    user = models.ForeignKey(User, unique=False, null=True, blank=True, default=None)
    completed = models.BooleanField(default=False)
    bounding_box = models.PolygonField(null=True, blank=True, srid=4326)

    objects = models.GeoManager() #enable geo-dealings

    def __unicode__(self):
        return "Section %d" % (self.index)

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
