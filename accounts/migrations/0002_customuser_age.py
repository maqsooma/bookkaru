# Generated by Django 4.1.7 on 2023-06-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]