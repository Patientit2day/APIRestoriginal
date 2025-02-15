# Generated by Django 5.0.6 on 2024-11-04 09:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0014_delete_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('adress', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=12)),
                ('contrat', models.FileField(blank=True, null=True, upload_to='pdf_contrats/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
