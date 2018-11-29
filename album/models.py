from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

def image_upload_method(instance, filename):
    return 'albums/{album}/{photo}'.format(album=instance.album, photo=filename)

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    file = models.ImageField(upload_to=image_upload_method, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file
