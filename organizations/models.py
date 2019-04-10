from django.db import models
from django.core.validators import *
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Organization(models.Model):
    LEVEL = (
        ("Main", "Main"),
        ("Core Subject", "Core Subject"),
        ("Social Science", "Social Science"),
        ("Music and Arts", "Music and Arts"),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(choices=LEVEL, max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to="organization/{}/logo".format(name), null=True)
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
        ], choices=SY_CHOICES
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