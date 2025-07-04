# Generated by Django 5.0.12 on 2025-06-15 07:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('small_title', models.CharField(blank=True, max_length=2555, null=True)),
                ('title', models.CharField(blank=True, max_length=2555, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Hero Section',
                'verbose_name_plural': 'Hero Sections',
            },
        ),
    ]
