# Generated by Django 4.2.6 on 2024-01-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='duration',
            field=models.IntegerField(default=22),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='total_rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]