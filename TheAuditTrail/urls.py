from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sections.views.list_sections', name='list_sections'),
    url(r'^map/', 'sections.views.view_map', name='view_map'),
    url(r'^toggleComplete/(?P<section_id>\d{0,3})/$', 'sections.views.toggle_complete', name='toggle_complete'),
    url(r'^toggleReserved/(?P<section_id>\d{0,3})/$', 'sections.views.toggle_reserved', name='toggle_reserved'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', CreateView.as_view(template_name='register.html', form_class=UserCreationForm, success_url='/')),
    #url(r'^login/', 'sections.views.login', name='login'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)
