# Generated by Django 4.2.3 on 2023-11-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='average_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_ratings',
            field=models.IntegerField(default=0),
        ),
    ]