from django.db import models
from django.core.validators import *
from django.utils import timezone
from django.urls import reverse

class ResearchPaper(models.Model):
    CATEGORY_CHOICES = (
        ("Applied", "Applied Science"),
        ("Life", "Life Science")
    )
    Applied = "Applied"
    Life = "Life"

    title = models.TextField()
    abstract = models.TextField()

    published_date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to="research_papers/{}".format(str(title).lower()), validators=[FileExtensionValidator(['pdf'])],)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50, default=None, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('staff:research')

    def __str__(self):
        return self.title + " - " + self.category

class ResearchProponent(models.Model):
    research = models.ForeignKey(ResearchPaper, on_delete=models.CASCADE, related_name="proponents")
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('staff:research')

    def __str__(self):
        return self.first_name + self.last_name
