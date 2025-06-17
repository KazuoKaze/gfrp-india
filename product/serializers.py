from rest_framework import serializers
from .models import CarouselImage, Application, SingleProduct, SingleProductSection, ProductPage


class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ['uuid', 'image']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['uuid', 'title', 'image']


class SingleProductSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(many=True, read_only=True)
    image = CarouselImageSerializer(many=True, read_only=True)

    class Meta:
        model = SingleProduct
        fields = ['uuid', 'title', 'description', 'tag', 'application', 'image']


class SingleProductSectionSerializer(serializers.ModelSerializer):
    single_products = SingleProductSerializer(many=True, read_only=True)

    class Meta:
        model = SingleProductSection
        fields = ['uuid', 'title', 'single_products']


class ProductPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPage
        fields = ['uuid', 'title', 'description', 'image']