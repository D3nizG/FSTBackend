from django.shortcuts import render
from django.shortcuts import render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fstmobile.serializers import ContactSerializer
from fstmobile.serializers import NewsSerializer
from fstmobile.serializers import ScholarshipSerializer
from fstmobile.models import Contact
from fstmobile.serializers import FAQSerializer
from fstmobile.models import FAQ
from fstmobile.models import News
from fstmobile.models import Scholarship

# Create your views here.

def index(request):
	return render_to_response('fstmobile/index.html')

class ListContacts(APIView):

	def get(self,request,format=None):

		contacts = Contact.objects.all()
		serializer = ContactSerializer(contacts,many=True)
		return Response(serializer.data)

class ListFAQs(APIView):

	def get(self,request,format=None):
		faqs = FAQ.objects.all()
		serializer = FAQSerializer(faqs,many=True)
		return Response(serializer.data)

class ListNews(APIView):

	def get(self,request,format=None):

		news = News.objects.all()
		serializer = NewsSerializer(news,many=True)
		return Response(serializer.data)

class ListScholarship(APIView):
	
	def get(self,request,format=None):

		scholarship = Scholarship.objects.all()
		serializer = ScholarshipSerializer(scholaraship,many=True)
		return Response(serializer.data)
