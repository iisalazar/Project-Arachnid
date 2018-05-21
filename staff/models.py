from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class FileUpload(models.Model):
    file = models.FileField(validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])
    def __str__(self):
        return self.file.url
