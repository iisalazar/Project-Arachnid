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

class NewsForm(forms.ModelForm):
    class Meta:
        model = models.News
        fields = ('author', 'author_additional_info', 'headline', 'headline_image', 'body_text', 'other_image')
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Name of the author (not required)'}),
            'author_additional_info': forms.TextInput(attrs={'class': 'textinputclass'}),
            'headline': forms.Textarea(attrs={'class': 'editable medium-editor-textarea', 'placeholder': 'Write headline'}),
            'body_text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
