![Build Status](https://api.travis-ci.org/JosephRedfern/TheAuditTrail.svg)


TheAuditTrail
=============

A tool for scheduling large-scale walks (built with the Wales Coastal path in mind) - allows users to register, see path sections that have been taken, and reserve sections of their own.

The Wales Coastal Path is currently split up into several regions, with each region contianing several sections (109 in total). These section are stored as WKT using GeoDjango, which are then passed into Leaflet using django-geojson to "translate" from WKT to GeoJSON. When a section is reserved, it turns yellow on the map, and once it's marked as completed, it turns Green. 

Technolgies
-----------
Built using Django, GeoDjango, django-geojson, and django-leaflet for mapping. 

Installation
------------
For the purposes of the hackathon, we've used an sqlite database backend with geospatial extentions - for instructions on how to set this up, check out: https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/spatialite/#create-spatialite-db. It would j

You'll also need to install the necessary python modules; this can be done by running "pip install -r requirements.txt" from within the TheAuditTrail directory.

Once the requirements have been installed, the project can be run with the command "python manage.py runserver" to get up and running quickly - refer to [How to deploy with WSGI](https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/)  Django documentation for a more long-term, robust solution. It's worth noting that this is currently "hackathon quality code", and may be riddled with bugs - here be dragons!
