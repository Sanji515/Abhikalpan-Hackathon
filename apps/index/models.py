from django.db import models

# Create your models here.

class Complaint(models.Model):
	title = models.CharField(max_length=100)
	meta_description = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title
