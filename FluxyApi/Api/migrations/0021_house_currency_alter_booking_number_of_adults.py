# Generated by Django 5.0.6 on 2024-11-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0020_alter_booking_maison_alter_booking_booking_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='currency',
            field=models.CharField(default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_adults',
            field=models.CharField(max_length=45),
        ),
    ]