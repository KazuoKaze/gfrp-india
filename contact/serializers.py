from rest_framework import serializers

from .models import ContactPage, ContactForm

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = ['uuid', 'title', 'description', 'image', 'phone', 'email_address', 'address']


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'