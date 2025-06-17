from django.shortcuts import render

# Create your views here.

from .models import HeroSection, AboutSection, SubSectionOfHowToStart, HowToStartSection, SingleProductionSection, SingleProduction, ProductionSection
from .serializers import HeroSectionSerializer, AboutSectionSerializer, SubSectionOfHowToStartSerializer, HowToStartSectionSerializer, SingleProductionSectionSerializer, SingleProductionSerializer, ProductionSectionSerializer

from rest_framework.decorators import api_view
from rest_framework import status


from rest_framework.response import Response

@api_view(['GET'])
def hero_section_list(request):
    hero = HeroSection.objects.first()
    serializer = HeroSectionSerializer(hero, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def about_section_list(request):
    about = AboutSection.objects.first()
    serializer = AboutSectionSerializer(about, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def how_to_start_section_list(request):
    how_to_start = HowToStartSection.objects.first()
    serializer = HowToStartSectionSerializer(how_to_start, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def production_section_list(request):
    production_section = ProductionSection.objects.first()
    serializer = ProductionSectionSerializer(production_section, context={'request': request})
    return Response(serializer.data)

