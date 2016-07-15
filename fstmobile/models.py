from django.db import models
import datetime

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=255)
	number = models.CharField(max_length=255)
	created = models.DateTimeField('auto_now_add=true',editable=False,default=datetime.datetime.now())

	def __str__(self):
		return self.name



class News(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=400)
	story = models.TextField()
	image_url = models.CharField(max_length=255)
	created = models.DateTimeField('auto_now_add=true',editable=False,default=datetime.datetime.now())

	def __str__(self):
		return self.title




