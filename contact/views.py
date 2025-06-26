from django.shortcuts import render

# Create your views here.

from .models import ContactPage, ContactForm
from .serializers import ContactSerializer, ContactFormSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from django.core.mail import send_mail


@api_view(['GET'])
def get_contact(request):
    contact = ContactPage.objects.first()
    serializer = ContactSerializer(contact, context={'request': request})
    return Response(serializer.data)


# @api_view(["POST"])
# def contact_form_view(request):
#     serializer = ContactFormSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Form submitted successfully!"}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def contact_form_view(request):
    print(request.data, 'this is data')
    serializer = ContactFormSerializer(data=request.data)
    if serializer.is_valid():
        contact = serializer.save()

        # Send email
        subject = "New Contact Form Submission"
        message = f"""
You have received a new contact form submission:

Name: {contact.first_name} {contact.last_name}
Email: {contact.email_address}
Phone: {contact.phone}
City: {contact.city}
Message: {contact.message}
"""
        send_mail(
            subject,
            message,
            'cvplindore@gmail.com',  # from
            ['gfrpindia@gmail.com'],  # to
            fail_silently=False,
        )

        return Response({"message": "Form submitted successfully!"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)