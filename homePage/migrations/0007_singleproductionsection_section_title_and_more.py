# Generated by Django 5.0.12 on 2025-06-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0006_alter_productionsection_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleproductionsection',
            name='section_title',
            field=models.CharField(blank=True, max_length=2555, null=True),
        ),
        migrations.DeleteModel(
            name='ProductionSection',
        ),
    ]
