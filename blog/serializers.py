from rest_framework import serializers

from .models import Author, Blog, BlogPage

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['uuid', 'name', 'profile_picture', 'created_at']

class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = [
            'uuid', 'tag', 'min_read', 'created_at', 'image', 'title',
            'slug', 'description', 'author'
        ]


class BlogDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    related_blogs = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = [
            'uuid', 'tag', 'min_read', 'created_at', 'image', 'title',
            'slug', 'description', 'author', 'content', 'related_blogs'
        ]


class BlogPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPage
        fields = ['uuid', 'title', 'description', 'image']