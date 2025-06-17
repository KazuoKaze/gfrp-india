from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SingleProductSection, ProductPage
from .serializers import SingleProductSectionSerializer, ProductPageSerializer


@api_view(['GET'])
def single_product_section_view(request):
    section = SingleProductSection.objects.first()  # or use get() if only one is expected
    serializer = SingleProductSectionSerializer(section, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def product_page_view(request):
    page = ProductPage.objects.first()
    serializer = ProductPageSerializer(page, context={'request': request})
    return Response(serializer.data)