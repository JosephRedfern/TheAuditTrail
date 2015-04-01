from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from pages.models import Page

class PageAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page

class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm

admin.site.register(Page, PageAdmin)
