# Generated by Django 5.0.12 on 2025-06-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_resourcespage'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcespage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='resources_page/'),
        ),
    ]
