# Generated by Django 4.2.7 on 2023-11-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
