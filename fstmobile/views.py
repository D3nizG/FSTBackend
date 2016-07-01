from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fstmobile.serializers import ContactSerializer
from fstmobile.models import Contact
# Create your views here.


class ListContacts(APIView):

	def get(self,request,format=None):

		contacts = Contact.objects.all()
		serializer = ContactSerializer(contacts,many=True)
		return Response(serializer.data)

