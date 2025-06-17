from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog, Author, BlogPage
from .serializers import AuthorSerializer, BlogSerializer, BlogDetailSerializer, BlogPageSerializer


@api_view(['GET'])
def blog_home_list_view(request):
    blogs = Blog.objects.filter(is_published=True).order_by('-created_at')
    serializer = BlogSerializer(blogs, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def blog_page_view(request):
    blog_page = BlogPage.objects.first() 
    serializer = BlogPageSerializer(blog_page, context={'request': request})
    return Response(serializer.data)



@api_view(['GET'])
def blog_detail_view(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=404)

    serializer = BlogDetailSerializer(blog, context={'request': request})
    return Response(serializer.data)