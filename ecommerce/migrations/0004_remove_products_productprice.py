# Generated by Django 2.2.6 on 2019-11-22 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_products_productimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='productPrice',
        ),
    ]