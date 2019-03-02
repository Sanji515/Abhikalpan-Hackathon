from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Complaint(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=100)
	meta_description = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return '{user}--{title}'.format(user=self.user, title=self.title)

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
	comment = models.TextField()
	commented_at = models.DateTimeField(auto_now_add=False, auto_now=False, default=timezone.now)

	def __str__(self):
		return '{user}--{complaint}'.format(user=self.user, complaint=self.complaint)
