# Generated by Django 5.0.3 on 2024-07-13 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_rename_name_category_category_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='features',
            new_name='featured',
        ),
    ]
