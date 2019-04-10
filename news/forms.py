from django import forms
from . import models
from django.core import validators

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
    