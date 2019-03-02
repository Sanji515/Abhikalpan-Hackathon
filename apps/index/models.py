from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Complaint(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=100)
	meta_description = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return '{user}--{title}'.format(user=self.user, title=self.title)
