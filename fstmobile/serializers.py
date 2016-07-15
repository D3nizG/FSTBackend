from fstmobile.models import Contact
from fstmobile.models import News
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = ('id','name','number')


class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ('id','created','title','description','image_url','story')