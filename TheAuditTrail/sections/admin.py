from django.contrib import admin
from .models import Region, Section
from leaflet.admin import LeafletGeoAdmin

admin.site.register(Region)
admin.site.register(Section, LeafletGeoAdmin)
