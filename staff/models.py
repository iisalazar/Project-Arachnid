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

class News(models.Model):
    author = models.CharField(max_length=100, blank=True)
    author_additional_info = models.CharField(max_length=100, blank=True)

    lead_text = models.TextField()


    #lead_text = models.CharField(max_length=10000, blank=True)
    #opening = models.CharField(max_length=10000)

    headline = models.CharField(max_length=200)
    headline_image = models.ImageField(upload_to="news_pictures/%Y/%m/%d", blank=True, null=True, validators=[FileExtensionValidator(['png', 'jpeg', 'jpg', 'JPG'])])

    headline = models.TextField()
    headline_image = models.ImageField(upload_to="news_pictures/%Y/%m/%d", blank=True, null=True)


    cover_photo = models.ImageField(upload_to="news_pictures/%Y/%m/%d/cover", blank=True, null=True)
    body_text = models.TextField()


    other_image = models.ImageField(upload_to="news_pictures/%Y/%m/%d", blank=True, null=True)
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

class Organization(models.Model):
    LEVEL = (
        ("Main", "Main"),
        ("Core Subject", "Core Subject"),
        ("Social Science", "Social Science"),
        ("Music and Arts", "Music and Arts"),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(choices=LEVEL, max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to="organization/" + str(name).lower() + "/logo", null=True)
    acronym = models.CharField(max_length=10)


    description = models.TextField(max_length=5000)

    def get_absolute_url(self):
        return reverse('staff:organizations')

    def __str__(self):
        return self.name

class OrganizationOfficer(models.Model):
    organization = models.ForeignKey(Organization, related_name="officers", on_delete=models.CASCADE)

    SY_CHOICES = [
        (x,x) for x in range(timezone.now().year-1, timezone.now().year+1)
    ]

    school_year = models.PositiveIntegerField(validators=[
        MinValueValidator(2018),
        MaxValueValidator(timezone.now().year)
        ], choices=SY_CHOICES,
    )

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

    adviser_picture = models.ImageField(upload_to="organiation/" + str(organization.name).lower() + "/profiles", null=True, blank=True)
    pres_picture = models.ImageField(upload_to="organization/" + str(organization.name).lower() + "/profiles", null=True, blank=True)
    vp_picture = models.ImageField(upload_to="organization/" + str(organization.name).lower() + "/profiles", null=True, blank=True)
    sec_picture = models.ImageField(upload_to="organization/" + str(organization.name).lower() + "/profiles", null=True, blank=True)
    tres_picture = models.ImageField(upload_to="organization/" + str(organization.name).lower() + "/profiles", null=True, blank=True)
    aud_picture = models.ImageField(upload_to="organization/" + str(organization.name) + "/profiles", null=True, blank=True)
    pio_picture = models.ImageField(upload_to="organization/" + str(organization.name) + "/profiles", null=True, blank=True)
    g7_picture = models.ImageField(upload_to="organization/" + str(organization.name) + "/profiles", null=True, blank=True)
    g8_picture = models.ImageField(upload_to="organization/" + str(organization.name) + "/profiles", null=True, blank=True)
    g9_picture = models.ImageField(upload_to="organization/" + str(organization.name) + "/profiles", null=True, blank=True)
    g10_picture = models.ImageField(upload_to="organization/" + str(organization.name) + "/profiles", null=True, blank=True)
    g11_picture = models.ImageField(upload_to="organization/" + str(organization.name) + "/profiles", null=True, blank=True)
    g12_picture = models.ImageField(upload_to="organization/" + str(organization.name) + "/profiles", null=True, blank=True)


    @property
    def is_present(self):
        if self.school_year > timezone.now().year:
            return False
        else:
            return True
    
    def get_all_of_them(self):
        # TODO
        # Add a method to return all person as a list
        pass
    def get_absolute_url(self):
        return reverse('staff:organization_details', pk=self.organization.pk)

    def __str__(self):
        return "Officers of " + self.organization.name + " for school year " + str(self.school_year)

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
