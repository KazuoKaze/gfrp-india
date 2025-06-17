from django.shortcuts import render

# Create your views here.

from .models import ContactPage
from .serializers import ContactSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_contact(request):
    contact = ContactPage.objects.first()
    serializer = ContactSerializer(contact, context={'request': request})
    return Response(serializer.data)