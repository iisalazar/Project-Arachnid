from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    file = models.FileField(blank=True, validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], upload_to="announcement_documents")
    date_created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('staff:announcements')
    def __str__(self):
        return self.title

class News(models.Model):
    author = models.CharField(max_length=100, blank=True)
    author_additional_info = models.CharField(max_length=100, blank=True)
    headline = models.CharField(max_length=200)
    headline_image = models.ImageField(upload_to="news_pictures/%Y/%m/%d", blank=True, null=True)
    body_text = models.CharField(max_length=10000)
    other_image = models.ImageField(upload_to="news_pictures/%Y/%m/%d", blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('staff:news')

    def __str__(self):
        return self.headline + "- Written by" +self.author
