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

def toggle_complete(request, section_id):
    section = Section.objects.get(index=int(section_id))
    if section.user is not None and section.completed:
        print "Owner is requesting un-completion"
        section.completed = not section.completed
        section.save()
    elif section and section.user == request.user:
        print "Logged-in user is requesting completion"
        section.completed = not section.completed
        section.save()
    else:
        print "invalid request"
    return HttpResponseRedirect("/")

def toggle_reserved(request, section_id):
    section = Section.objects.get(index=int(section_id))
    if section.user is None and request.user.is_authenticated():
        print "Valid user, reserving section %s" % (section_id)
        section.user = request.user
        section.save()

    elif (section.user == request.user):
        print "Valid Request, toggling reservation"
        section.user = None
        section.save()

    return HttpResponseRedirect("/")


