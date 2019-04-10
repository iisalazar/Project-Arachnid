from django.db import models
from django.core.validators import *
from django.utils import timezone
from django.urls import reverse
# Create your models here.
from django.utils.html import strip_tags
# Create your models here.


def news_image_handler(instance, filename):
    _instance = instance
    headline = strip_tags(instance.headline)
    return "news/{year}/{headline}/{filename}".format(year=timezone.now().year, headline=headline, filename=filename)

class News(models.Model):
    author = models.CharField(max_length=100, blank=True)
    author_additional_info = models.CharField(max_length=100, blank=True)

    lead_text = models.TextField()

    #lead_text = models.CharField(max_length=10000, blank=True)
    opening = models.CharField(max_length=10000, blank=True)

    headline = models.CharField(max_length=200)
    # Saves the image to /media/news/YEAR-CREATED/HEADLINE/
    headline_image = models.ImageField(upload_to=news_image_handler, validators=[FileExtensionValidator(['png', 'jpeg', 'jpg', 'JPG'])])

    # Saves the image to /media/news/YEAR-CREATED/HEADLINE/
    cover_photo = models.ImageField(upload_to=news_image_handler, blank=True, null=True)
    body_text = models.TextField()

    # Saves the image to /media/news/YEAR-CREATED/HEADLINE/
    other_image = models.ImageField(upload_to=news_image_handler, blank=True, null=True)
    other_image_label = models.CharField(max_length=250, blank=True, null=True)


    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('staff:news')

    def __str__(self):
        return self.headline + "- Written by" +self.author