from django import forms
from . import models

class FileFieldForm(forms.ModelForm):

    class Meta:
        model = models.FileUpload
        fields = '__all__'
