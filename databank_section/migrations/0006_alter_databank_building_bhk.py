# Generated by Django 5.1.6 on 2025-05-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databank_section', '0005_databank_care_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databank',
            name='building_bhk',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
