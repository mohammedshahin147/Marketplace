# Generated by Django 4.2.6 on 2024-01-11 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_alter_booking_tenant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_rate',
            field=models.BigIntegerField(),
        ),
    ]
