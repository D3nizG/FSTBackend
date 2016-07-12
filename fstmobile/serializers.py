from fstmobile.models import Contact
from fstmobile.models import FAQ
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = ('id','name','number')

class FAQSerializer(serializers.ModelSerializer):
	class Meta:
		model = FAQ
		fields  = ('id','question','answer')
