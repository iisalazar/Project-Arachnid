from django import forms
from . import models
from django.core import validators

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