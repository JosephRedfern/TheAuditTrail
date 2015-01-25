from django.shortcuts import render, render_to_response, HttpResponseRedirect
from models import Section, Region
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def list_sections(request):
    values = {}

    values['sections'] = Section.objects.all()

    return render(request, 'sections.html', values)


def view_map(request):
    values = {}
    sections = Section.objects.all()

    mapPoints = []

    for section in sections:
        colour = "#FFFFFF"
        if section.completed:
            colour = "#00AA00"
        elif section.user is not None:
            colour = "#FFFF00"
        else:
            colour = "#FF0000"

        mapPoints.append({'id': section.id, 'region':section.region.name, 'colour':colour, 'polygon':section.bounding_box})

    values['areas'] = mapPoints

    return render(request, 'map.html', values)
