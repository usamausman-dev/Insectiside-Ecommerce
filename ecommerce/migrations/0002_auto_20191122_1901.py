# Generated by Django 2.2.6 on 2019-11-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='discountedPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='marketPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]