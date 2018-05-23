from django import forms
from . import models

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = models.Announcement
        fields = ('title', 'description', 'file')
        widgets = {
        	'title': forms.TextInput(),
        	'description': forms.Textarea(),
        	'file': forms.FileInput()
        }
