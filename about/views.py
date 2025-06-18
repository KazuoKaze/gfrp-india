from django.shortcuts import render

# Create your views here.
from .models import AboutHeroSection, AboutOurStorySection, AboutValues, WholeWhySection

from .serializers import AboutHeroSectionSerializer, AboutStorySectionSerializer, AboutValueSerializer, AboutWholeWhySerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_about_hero(request):
    contact = AboutHeroSection.objects.first()
    serializer = AboutHeroSectionSerializer(contact, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def get_about_story(request):
    contact = AboutOurStorySection.objects.first()
    serializer = AboutStorySectionSerializer(contact, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def get_value(request):
    contact = AboutValues.objects.all()
    serializer = AboutValueSerializer(contact, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def get_why(request):
    contact = WholeWhySection.objects.first()
    serializer = AboutWholeWhySerializer(contact, context={'request': request})
    return Response(serializer.data)