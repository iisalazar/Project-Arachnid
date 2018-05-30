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

class Organization(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="organization/" + str(name).lower() + "/logo", null=True)
    acronym = models.CharField(max_length=10)
    adviser = models.CharField(max_length=100)
    president = models.CharField(max_length=100)
    vice_president = models.CharField(max_length=100)
    secretary = models.CharField(max_length=100)
    treasurer = models.CharField(max_length=100)
    auditor = models.CharField(max_length=100)
    pio = models.CharField(max_length=100)
    g7_rep = models.CharField(max_length=100)
    g8_rep = models.CharField(max_length=100)
    g9_rep = models.CharField(max_length=100)
    g10_rep = models.CharField(max_length=100)
    g11_rep = models.CharField(max_length=100)
    g12_rep = models.CharField(max_length=100)

    adviser_picture = models.ImageField(upload_to="organiation/" + str(name).lower() + "/profiles", null=True, blank=True)
    pres_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    vp_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    sec_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    tres_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    aud_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    pio_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    g7_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    g8_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    g9_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    g10_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    g11_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)
    g12_picture = models.ImageField(upload_to="organization/" + str(name).lower() + "/profiles", null=True, blank=True)


    #org_pictures = models.ImageField(upload_to="organization/" + str(name).lower() + "/pictures", null=True)
    description = models.CharField(max_length=1000, blank=True)

    def get_absolute_url(self):
        return reverse('staff:organizations')

    def __str__(self):
        return self.name

class ResearchPaper(models.Model):
    CATEGORY_CHOICES = (
        ("Applied", "Applied Science"),
        ("Life", "Life Science")
    )
    Applied = "Applied"
    Life = "Life"
    title = models.CharField(max_length=500)
    abstract = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to="research_papers/" + str(title).lower(), validators=[FileExtensionValidator(['pdf'])],)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50, default=None)

    def get_absolute_url(self):
        return reverse('staff:research')

    def __str__(self):
        return self.title + " - " + self.category

class ResearchPaperProponents(models.Model):
    research = models.ForeignKey(ResearchPaper, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('staff:research')

    def __str__(self):
        return self.first_name + self.last_name
