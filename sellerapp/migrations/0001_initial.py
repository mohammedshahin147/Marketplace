# Generated by Django 4.2.6 on 2024-01-10 05:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('rented', models.BooleanField(default=False)),
                ('available_from', models.DateField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('villa', 'Villa'), ('house', 'House'), ('apartment', 'Apartment')], max_length=15)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sellerapp.property')),
                ('bedroom_type', models.CharField(choices=[('1BHK', '1 Bedroom, Hall, Kitchen, 2 Car Parking'), ('2BHK', '2 Bedrooms, Hall, Kitchen, 2 Car Parking'), ('3BHK', '3 Bedrooms, Hall, Kitchen, 2 Car Parking'), ('4BHK', '4 Bedrooms, Hall, Kitchen, 2 Car Parking')], max_length=12)),
            ],
            bases=('sellerapp.property',),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sellerapp.property')),
                ('bedroom_type', models.CharField(choices=[('1BHK', '1 Bedroom, Hall, Kitchen, 1 Car Parking'), ('2BHK', '2 Bedrooms, Hall, Kitchen, 1 Car Parking'), ('3BHK', '3 Bedrooms, 2 Hall, Kitchen, 2 Car Parking'), ('4BHK', '4 Bedrooms, 2 Hall, 2 Kitchen, 3 Car Parking'), ('5BHK', '5 Bedrooms, 2 Hall, 2 Kitchen, 4 Car Parking')], max_length=12)),
            ],
            bases=('sellerapp.property',),
        ),
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sellerapp.property')),
                ('bedroom_type', models.CharField(choices=[('2BHK', '2 Bedrooms, 2 Hall, 2 Kitchen, 4 Car Parking'), ('3BHK', '3 Bedrooms, 2 Hall, 2 Kitchen, 5 Car Parking'), ('4BHK', '4 Bedrooms, 2 Hall, 2 Kitchen, 6 Car Parking'), ('5BHK', '5 Bedrooms, 2 Hall, 2 Kitchen, 8 Car Parking')], max_length=12)),
            ],
            bases=('sellerapp.property',),
        ),
    ]