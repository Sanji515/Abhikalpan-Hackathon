from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Company(models.Model):
	company_name = models.CharField(max_length=200)

	def __str__(self):
		return self.company_name


class Complaint(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=100)
	meta_description = models.CharField(max_length=200)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=False, auto_now=False, default=timezone.now)

	def __str__(self):
		return '{user}--{title}'.format(user=self.user, title=self.title)


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	complaint = models.ForeignKey(Complaint, related_name='for_complaint', on_delete=models.CASCADE)
	comment = models.TextField()
	commented_at = models.DateTimeField(auto_now_add=False, auto_now=False, default=timezone.now)

	def __str__(self):
		return '{user}--{complaint}'.format(user=self.user, complaint=self.complaint)

class Like(models.Model):
	complaint = models.ForeignKey(Complaint, related_name='like_complaint', on_delete=models.CASCADE)
	liked_by = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{liked_by}--{complaint}'.format(
			liked_by=self.liked_by,
			complaint=self.complaint)
