from django import forms
from . import models
from django.core import validators


CATEGORY_CHOICES = (
    ("Applied", "Applied Science"),
    ("Life", "Life Science")
)

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
