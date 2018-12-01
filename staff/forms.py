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
        fields = ('author', 'author_additional_info', 'lead_text', 'headline', 'headline_image', 'cover_photo', 'body_text', 'other_image', 'other_image_label')
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Name of the author (not required)'}),

            'author_additional_info': forms.TextInput(attrs={'class': 'textinputclass'}),

            'lead_text': forms.Textarea(attrs={'placeholder': 'Write here the lead paragraph/sentence', }),

            'headline': forms.Textarea(attrs={'class': 'editable medium-editor-textarea', 'placeholder': 'Write headline'}),

            'body_text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),

            'other_image_label': forms.TextInput(attrs={'placeholder': 'Write label for other image'})
        }

LEVEL = (
    ("Main", "Main"),
    ("Core Subject", "Core Subject"),
    ("Social Science", "Social Science"),
    ("Music and Arts", "Music and Arts"),
)

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of Organization'}),
            'category': forms.Select(choices=LEVEL),
            'acronym': forms.TextInput(attrs={'placeholder': 'E.g. RobITech, YAG'}),
            'description': forms.Textarea(),
        }

CATEGORY_CHOICES = (
    ("Applied", "Applied Science"),
    ("Life", "Life Science")
)

# For organization HR
class OrganizationHRForm(forms.ModelForm):
    class Meta:
        model = models.OrganizationOfficer
        exclude  = ('organization', )
        widgets = {
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
        }

class ResearchForm(forms.ModelForm):
    class Meta:
        model = models.ResearchPaper
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'abstract': forms.Textarea(),
            'published_date': forms.DateInput(),
            'category': forms.Select(choices=CATEGORY_CHOICES)
        }

class ResearchProponentForm(forms.ModelForm):
    class Meta:
        model = models.ResearchProponent
        fields = ('first_name', 'middle_name', 'last_name')
