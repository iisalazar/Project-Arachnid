from django import forms
from .models import Album, Image

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ('title', 'description', 'date_published')
		widgets = {
			'title': forms.TextInput(attrs={'placeholder': 'Title of the Album'}),
			'description' : forms.Textarea(attrs={'placeholder' : 'Description for the album'}),
		}

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ('image',)

		