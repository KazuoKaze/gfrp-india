from rest_framework import serializers

from .models import ContactPage

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = ['uuid', 'title', 'description', 'image', 'phone', 'email_address', 'address']