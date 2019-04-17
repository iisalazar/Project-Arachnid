from django import forms
from .models import Album, Photo

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title','description')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file',)
