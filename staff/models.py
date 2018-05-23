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
