from django.db import models
import datetime

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=255)
	number = models.CharField(max_length=255)
	created = models.DateTimeField('auto_now_add=true',editable=False,default=datetime.datetime.now())

	def __str__(self):
		return self.name

class FAQ(models.Model):
	question = models.CharField(max_length=255);
	answer = models.CharField(max_length=255);

	def __str__(self):
		return self.question

class News(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=400)
	story = models.TextField()
	image_url = models.CharField(max_length=255)
	created = models.DateTimeField('auto_now_add=true',editable=False,default=datetime.datetime.now())

	def __str__(self):
		return self.title


class Scholarship(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=400)
	detail = models.TextField()
	created = models.DateTimeField('auto_now_add=true',editable=False,default=datetime.datetime.now())

	def __str__(self):
		return self.name

class Place(models.Model):
	fullname = models.CharField(max_length=255)
	shortname = models.CharField(max_length=255)
	department = models.CharField(max_length=255)
	location = models.CharField(max_length=50)

	def __str__(self):
		return self.shortname
