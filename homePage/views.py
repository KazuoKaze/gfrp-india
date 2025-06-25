from django.shortcuts import render

# Create your views here.

from .models import HeroSection, AboutSection, SubSectionOfHowToStart, HowToStartSection, SingleProductionSection, SingleProduction, ProductionSection, FAQSection, NewsLetter
from .serializers import HeroSectionSerializer, AboutSectionSerializer, SubSectionOfHowToStartSerializer, HowToStartSectionSerializer, SingleProductionSectionSerializer, SingleProductionSerializer, ProductionSectionSerializer, FaqSectionSerializer, NewsLetterSectionSerializer

from rest_framework.decorators import api_view
from rest_framework import status


from rest_framework.response import Response

@api_view(['GET'])
def hero_section_list(request):
    hero = HeroSection.objects.first()
    serializer = HeroSectionSerializer(hero, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def faq_section_list(request):
    hero = FAQSection.objects.all()
    serializer = FaqSectionSerializer(hero, many=True, context={'request': request})
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

@api_view(["POST"])
def newsletter_form_view(request):
    serializer = NewsLetterSectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Form submitted successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)