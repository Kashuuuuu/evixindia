# Generated by Django 4.0.2 on 2022-05-09 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_remove_product_image4'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product',
            new_name='products',
        ),
    ]
