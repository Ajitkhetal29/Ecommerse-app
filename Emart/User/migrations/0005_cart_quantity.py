# Generated by Django 4.2.3 on 2023-11-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
