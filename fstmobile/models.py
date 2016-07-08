from django.db import models
import datetime

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=255);
	number = models.CharField(max_length=255);
	created = models.DateTimeField('auto_now_add=true',editable=True,default=datetime.datetime.now());

	def __str__(self):
		return self.name



