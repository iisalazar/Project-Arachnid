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

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of Organization'}),
            'acronym': forms.TextInput(attrs={'placeholder': 'E.g. RobITech, YAG'}),
            'adviser': forms.TextInput(),
            'president': forms.TextInput(),
            'vice_president': forms.TextInput(),
            'secretary': forms.TextInput(),
            'treasurer': forms.TextInput(),
            'auditor': forms.TextInput(),
            'pio': forms.TextInput(),
            'g7_rep': forms.TextInput(),
            'g8_rep': forms.TextInput(),
            'g9_rep': forms.TextInput(),
            'g10_rep': forms.TextInput(),
            'g11_rep': forms.TextInput(),
            'g12_rep': forms.TextInput(),
            'description': forms.Textarea(),
        }
