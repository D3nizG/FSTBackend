from fstmobile.models import Contact
from fstmobile.models import FAQ
from fstmobile.models import News
from fstmobile.models import Scholarship
from fstmobile.models import Place
from fstmobile.models import Event
from fstmobile.models import Image
from fstmobile.models import Alert
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = ('id','name','number','email','website')

class FAQSerializer(serializers.ModelSerializer):
	class Meta:
		model = FAQ
		fields  = ('id','question','answer')

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ('id','created','title','description','image_url','story','news_url')

class ScholarshipSerializer(serializers.ModelSerializer):
        class Meta:
                model = Scholarship
                fields = ('id', 'name','description', 'detail','application_url')

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('id','fullname','shortname','department','location')

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ('id','title','date','description')

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ('id','name','url')

class AlertSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alert
		fields = {'id','title','description'}
		
