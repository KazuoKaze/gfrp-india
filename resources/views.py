from django.shortcuts import render

# Create your views here.
from .models import TechnicalResourceSection, TechnicalResources, ResourcesPage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TechnicalResourceSectionSerializer, TechnicalResourcesSerializer, ResourcesPageSerializer

@api_view(['GET'])
def technical_resource_section_view(request):
    sections = TechnicalResourceSection.objects.first()
    serializer = TechnicalResourceSectionSerializer(sections, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def technical_resources_view(request):
    resources = ResourcesPage.objects.first()
    serializer = ResourcesPageSerializer(resources, context={'request': request})
    return Response(serializer.data)


