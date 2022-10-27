# Generated by Django 4.0.7 on 2022-10-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_coupon_usedcoupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Pending', 'Pending')], default='New', max_length=20),
        ),
    ]
