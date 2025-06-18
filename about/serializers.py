from .models import HeroImage, AboutHeroSection, AboutOurStorySection, AboutSingleWhy, AboutValues, WholeWhySection

from rest_framework import serializers

class AboutHeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroImage
        fields = ['uuid', 'image']


class AboutHeroSectionSerializer(serializers.ModelSerializer):
    image = AboutHeroImageSerializer(many=True, read_only=True)
    class Meta:
        model = AboutHeroSection
        fields = ['uuid', 'title', 'description', 'image']


class AboutStorySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutOurStorySection
        fields = ['uuid', 'title', 'description', 'image']


class AboutValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutValues
        fields = ['uuid', 'title', 'description']


class AboutSingleWhySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSingleWhy
        fields = ['uuid', 'title', 'description']


class AboutWholeWhySerializer(serializers.ModelSerializer):
    why = AboutSingleWhySerializer(many=True, read_only=True)
    class Meta:
        model = WholeWhySection
        fields = ['uuid', 'title', 'description', 'why']

