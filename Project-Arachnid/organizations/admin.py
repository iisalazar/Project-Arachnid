from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Organization)
admin.site.register(models.OrganizationOfficer)