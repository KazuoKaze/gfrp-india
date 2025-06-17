from rest_framework import serializers

from .models import TechnicalResources, TechnicalResourceSection, ResourcesPage

class TechnicalResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalResources
        fields = ['uuid', 'title', 'description', 'file', 'created_at']
        
class TechnicalResourceSectionSerializer(serializers.ModelSerializer):
    technical_resources = TechnicalResourcesSerializer(many=True, read_only=True)

    class Meta:
        model = TechnicalResourceSection
        fields = ['uuid', 'title', 'description', 'technical_resources', 'created_at']

class ResourcesPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourcesPage
        fields = ['uuid', 'title', 'description', 'image']