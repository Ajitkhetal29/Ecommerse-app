# Generated by Django 4.2.3 on 2023-12-01 05:58

import Product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name=Product.models.Product),
        ),
    ]
