from django.shortcuts import render, render_to_response, HttpResponseRedirect
from models import Section, Region
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def list_sections(request):
    values = {}

    values['sections'] = Section.objects.all()

    return render(request, 'sections.html', values)
