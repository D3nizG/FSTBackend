from django.shortcuts import render
from django.shortcuts import render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fstmobile.serializers import ContactSerializer
from fstmobile.serializers import NewsSerializer
from fstmobile.serializers import ScholarshipSerializer
from fstmobile.serializers import FAQSerializer
from fstmobile.serializers import PlaceSerializer
from fstmobile.serializers import EventSerializer
from fstmobile.models import Contact
from fstmobile.models import FAQ
from fstmobile.models import News
from fstmobile.models import Scholarship
from fstmobile.models import Place
from fstmobile.models import Event

# Create your views here.

def index(request):
	return render_to_response('fstmobile/index.html')

class ListContacts(APIView):

	def get(self,request,format=None):

		contacts = Contact.objects.all()
		serializer = ContactSerializer(contacts,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = ContactSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ListFAQs(APIView):

	def get(self,request,format=None):
		faqs = FAQ.objects.all()
		serializer = FAQSerializer(faqs,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = FAQSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ListNews(APIView):

	def get(self,request,format=None):

		news = News.objects.all()
		serializer = NewsSerializer(news,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = NewsSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ListScholarship(APIView):

	def get(self,request,format=None):

		scholarship = Scholarship.objects.all()
		serializer = ScholarshipSerializer(scholarship,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = ScholarshipSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ListPlaces(APIView):

	def get(self,request,format=None):

		places = Place.objects.all();
		serializer = PlaceSerializer(places,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = PlaceSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ListEvents(APIView):

	def get(self,request,format=None):
		events = Event.objects.all()
		serializer = EventSerializer(events,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = EventSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


