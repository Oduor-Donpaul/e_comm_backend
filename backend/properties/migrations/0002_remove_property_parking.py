# Generated by Django 4.2.7 on 2023-11-29 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='parking',
        ),
    ]
