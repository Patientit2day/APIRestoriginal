# Generated by Django 5.0.6 on 2024-11-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stagiaires',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='pdf_contrats/'),
        ),
    ]
