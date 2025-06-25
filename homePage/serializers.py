from rest_framework import serializers

from .models import HeroSection, AboutSection, SubSectionOfHowToStart, HowToStartSection, SingleProductionSection, SingleProduction, ProductionSection, FAQSection, NewsLetter


class HeroSectionSerializer(serializers.ModelSerializer):   
    class Meta:
        model = HeroSection
        fields = ['uuid', 'small_title', 'title', 'description', 'image']


class FaqSectionSerializer(serializers.ModelSerializer):   
    class Meta:
        model = FAQSection
        fields = ['uuid', 'question', 'answer']


class NewsLetterSectionSerializer(serializers.ModelSerializer):   
    class Meta:
        model = NewsLetter
        fields = ['uuid', 'email']

class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = ['uuid', 'testimonial_title', 'image', 'image2', 'title', 'description']


class SubSectionOfHowToStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSectionOfHowToStart
        fields = ['uuid', 'title', 'description']

class HowToStartSectionSerializer(serializers.ModelSerializer):     
    sub_sections = SubSectionOfHowToStartSerializer(many=True, read_only=True)

    class Meta:
        model = HowToStartSection
        fields = ['uuid', 'title', 'description', 'image', 'sub_sections']


# class SingleProductionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SingleProduction
#         fields = ['uuid', 'title']

# class SingleProductionSectionSerializer(serializers.ModelSerializer):
#     single_productions = SingleProductionSerializer(many=True, read_only=True)

#     class Meta:
#         model = SingleProductionSection
#         fields = ['uuid', 'title', 'description', 'image', 'single_productions']

# class ProductionSectionSerializer(serializers.ModelSerializer):
#     single_production_sections = SingleProductionSectionSerializer(many=True, read_only=True)

#     class Meta:
#         model = ProductionSection
#         fields = ['uuid', 'title', 'single_production_sections']


class SingleProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleProduction
        fields = ['uuid', 'title']


class SingleProductionSectionSerializer(serializers.ModelSerializer):
    sections = SingleProductionSerializer(source="single_production", many=True, read_only=True)

    class Meta:
        model = SingleProductionSection
        fields = ['uuid', 'title', 'description', 'image', 'sections']


class ProductionSectionSerializer(serializers.ModelSerializer):
    production_sections = SingleProductionSectionSerializer(source="production", many=True, read_only=True)

    class Meta:
        model = ProductionSection
        fields = ['uuid', 'title', 'production_sections']