from django.db import models
import datetime
from django.utils import timezone
from pyfcm import FCMNotification

# Create your models here.

push_service = FCMNotification(api_key="AIzaSyABxZFZP7rGIh8WEcLHUTr-_WFfF3PsgNg")


class Contact(models.Model):
	name = models.CharField(max_length=255)
	number = models.CharField(max_length=255)
	email = models.CharField(max_length=255,default='None')
	website = models.CharField(max_length=255,default='None')

	def __str__(self):
		return self.name

class FAQ(models.Model):
	question = models.CharField(max_length=255);
	answer = models.TextField();

	def __str__(self):
		return self.question

	def __unicode__(self):
		return self.question
         
class News(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=400)
	story = models.TextField()
	image_url = models.CharField(max_length=255)
	created = models.DateTimeField('auto_now_add=true',editable=False,default=timezone.now())
	news_url = models.CharField(max_length=255,default='None')

	def save(self,force_insert=False,force_update=False,using=None):
		if(not self.id):
			topic_name = "news"
			message_title = "New news story"
			message_body = self.title
			data_message = {"activity" : "News"}
			result = push_service.notify_topic_subscribers(topic_name=topic_name,message_title=message_title,message_body=message_body,data_message=data_message)
			
		super(News,self).save()


	def __str__(self):
		return self.title


class Scholarship(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=400)
	detail = models.TextField(default='None')
	application_url = models.CharField(max_length=400,default='None')

	def __str__(self):
		return self.name

class Place(models.Model):
	fullname = models.CharField(max_length=255)
	shortname = models.CharField(max_length=255)
	department = models.CharField(max_length=255)
	location = models.CharField(max_length=2000)

	def __str__(self):
		return self.shortname

class Event(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateTimeField()
	description = models.TextField()

	def __str__(self):
		return self.title

class Image(models.Model):
	name = models.CharField(max_length=255)
	url = models.CharField(max_length=2000)
	
	#def save(self,force_insert=False,force_update=False,using=None):
	#	if(not self.id):
	#		topic_name = "gallery"
	#		message_title = "FaST Mobile"
	#		message_body = "New images"
	#		data_message = {"activity" : "Gallery"}
	#		result = push_service.notify_topic_subscribers(topic_name=topic_name,message_title=message_title,message_body=message_body,data_message=data_message)
				
	#	super(Image,self).save()

	def __str__(self):
		return self.name


class Alert(models.Model):
	
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.DateTimeField('auto_now_add=true',editable=False,default=timezone.now())

	def save(self,force_insert=False,force_update=False,using=None):
		if(not self.id):
			topic_name = "alerts"
			message_title = "New Alert"
			message_body = self.title
			data_message = {"activity" : "Alerts"}
			result = push_service.notify_topic_subscribers(topic_name=topic_name,message_title=message_title,message_body=message_body,data_message=data_message)
		super(Alert,self).save()

	def __str__(self):
		return self.title


