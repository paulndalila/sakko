# Generated by Django 4.1.7 on 2023-03-16 11:23

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KE')),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Milk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mFarm.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='MilkStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('fresh', 'Fresh'), ('spoilt', 'Spoilt')], default='fresh', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Sacco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MilkEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('butter_fat', models.FloatField()),
                ('protein_content', models.FloatField()),
                ('quantity_supplied', models.FloatField()),
                ('gross_price', models.FloatField()),
                ('the_milk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mFarm.milk')),
            ],
        ),
        migrations.CreateModel(
            name='MilkCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCollected', models.DateTimeField(auto_now_add=True)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mFarm.milkevaluation')),
                ('farmerCollected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mFarm.farmer')),
            ],
        ),
        migrations.AddField(
            model_name='milk',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mFarm.milkstatus'),
        ),
        migrations.AddField(
            model_name='farmer',
            name='sacco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mFarm.sacco'),
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_period', models.DateField()),
                ('amount', models.FloatField()),
                ('quantity', models.FloatField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mFarm.farmer')),
            ],
        ),
    ]
