from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode


class Notes(models.Model):
	user = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class signup(models.Model):
	first_name = models.CharField(max_length = 100, null=False,blank=False)
	middle_name = models.CharField(max_length=100,null=True,blank=True)
	last_name = models.CharField(max_length=100,null=False,blank=False)
	email = models.EmailField(null=False,blank=False)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)

	def __unicode__(self):
		return smart_unicode(self.email)
	def __str__(self):
		return self.email

# class comment(models.Model):
# 
# class post(models.Model):
# 
# class chapter(models.Model):
# 
# class question(models.Model):
# 
# class submission(models.Model):
# 	
# class notification(models.Model):

	
