# Generated by Django 5.1.6 on 2025-03-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_remove_product_description_remove_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='des',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10),
            preserve_default=False,
        ),
    ]
