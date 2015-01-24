from django.shortcuts import render, render_to_response
from models import Section, Region, Event, Registration

# Create your views here.

def list_sections(request):
    values = {}
    registrations = Registration.objects.all()

    values['registrations'] = registrations

    return render_to_response('sections.html', values)
