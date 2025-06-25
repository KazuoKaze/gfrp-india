from django.shortcuts import render

# Create your views here.

from .models import ContactPage, ContactForm
from .serializers import ContactSerializer, ContactFormSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status


@api_view(['GET'])
def get_contact(request):
    contact = ContactPage.objects.first()
    serializer = ContactSerializer(contact, context={'request': request})
    return Response(serializer.data)


@api_view(["POST"])
def contact_form_view(request):
    serializer = ContactFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Form submitted successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
