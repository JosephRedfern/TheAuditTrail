from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models

# Create your models here.

class Section(models.Model):
    index = models.IntegerField(unique=True)
    region = models.ForeignKey('Region')
    user = models.ForeignKey(User, unique=False, null=True, blank=True, default=None)
    completed = models.BooleanField(default=False)
    bounding_box = models.PolygonField(null=True, blank=True, srid=4326)

    objects = models.GeoManager() #enable geo-dealings

    class Meta:
        ordering = ["index"]

    def __unicode__(self):
        return "%s: Section %d" % (self.region.name, self.index)

class Region(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.name
