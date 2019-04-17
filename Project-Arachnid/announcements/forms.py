from django import forms
from . import models
from django.core import validators

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = models.Announcement
        fields = ('title', 'description', 'file')
        widgets = {
        	'title': forms.TextInput(),
        	'description': forms.Textarea(),
        	'file': forms.FileInput()
        }