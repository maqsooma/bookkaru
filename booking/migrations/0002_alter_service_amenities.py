# Generated by Django 4.1.7 on 2023-06-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='amenities',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]