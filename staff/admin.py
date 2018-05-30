from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Announcement)
admin.site.register(models.News)
admin.site.register(models.Organization)
admin.site.register(models.ResearchPaper)
admin.site.register(models.ResearchPaperProponents)
