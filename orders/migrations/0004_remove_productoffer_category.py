# Generated by Django 4.0.7 on 2022-10-17 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_productoffer_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoffer',
            name='category',
        ),
    ]
