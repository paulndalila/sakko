# Generated by Django 4.2 on 2023-04-05 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mFarm', '0003_milk_datecollected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milk',
            name='dateCollected',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
