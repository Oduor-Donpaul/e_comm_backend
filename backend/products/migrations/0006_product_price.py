# Generated by Django 4.2.7 on 2023-11-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_thumbnails_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=99.0, max_digits=15),
        ),
    ]