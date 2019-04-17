from django.db import models
from django.db import models
from django.core.validators import *
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=21845)
    file = models.FileField(blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])], upload_to="announcement_documents")
    date_created = models.DateTimeField(default=timezone.now)

    def is_recent(self):
        if timezone.now().day <= self.date_created.day + 1 :
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('staff:announcements')
    def __str__(self):
        return self.title
