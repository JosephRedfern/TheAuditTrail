from django.shortcuts import render, render_to_response
from models import Section, Region

# Create your views here.

def list_sections(request):
    values = {}

    values['sections'] = Section.objects.all()

    return render_to_response('sections.html', values)
