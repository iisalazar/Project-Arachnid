from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.


# A model for the album
class Album(models.Model):
	title = models.CharField(max_length=100)
	date_published = models.DateTimeField(default=timezone.now)
	description = models.CharField(max_length=1000)

	def get_absolute_url(self):
		return ("staff:index")

	def __str__(self):
		return ("Title: {}".format(self.title))

def get_image_filename(instance, filename):
	title = instance.album.title
	slug = slugify(title)
	return "album_images/{}-{}".format(slug, filename)

class Image(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')