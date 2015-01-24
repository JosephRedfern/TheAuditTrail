from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sections.views.list_sections', name='list_sections'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^register/', CreateView.as_view(template_name='register.html', form_class=UserCreationForm, success_url='/')),
    url('^accounts/', include('django.contrib.auth.urls')),
)
