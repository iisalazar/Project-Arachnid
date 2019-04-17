from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# For image compression
from io import BytesIO
from PIL import Image
from django.core.files import File


# To compress images
def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=70) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image

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
    return 'albums/{album}/{photo}'.format(album=instance.album.slug, photo=filename)

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name="photos")
    file = models.ImageField(upload_to=image_upload_method, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        try:
            new_image = compress(self.file)
            self.file = new_image
        except IOError as error:
            print(error)
            raise ValidationError('Invalid Image Format')
        return super().save(*args, **kwargs)