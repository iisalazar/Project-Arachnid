from django.db import models
from django.contrib.auth.hashers import check_password as def_check_password, make_password
from django.utils import timezone
# Create your models here.

class AdmissionAccount(models.Model):
	email = models.EmailField()
	password = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)


	def set_password(self, password):
		hashed_password = make_password(self.password)
		self.password = hashed_password


	def check_password(self, *args, **kwargs):
		return def_check_password(*args, **kwargs)



	def __str__(self):
		return self.email