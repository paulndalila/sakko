# Generated by Django 4.2 on 2023-04-19 08:50

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mFarm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sacco',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KE'),
        ),
    ]