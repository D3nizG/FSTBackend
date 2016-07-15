from fstmobile.models import Contact
from fstmobile.models import FAQ
from fstmobile.models import News
from fstmobile.models import Scholarship
from fstmobile.models import Place
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = ('id','name','number')

class FAQSerializer(serializers.ModelSerializer):
	class Meta:
		model = FAQ
		fields  = ('id','question','answer')

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ('id','created','title','description','image_url','story')

class ScholarshipSerializer(serializers.ModelSerializer):
        class Meta:
                model = Scholarship
                fields = ('id', 'name','description', 'detail', 'image_url')

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('id','fullname','shortname','department','location')
		
