# Generated by Django 4.2.3 on 2023-07-29 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='time_required',
        ),
    ]
