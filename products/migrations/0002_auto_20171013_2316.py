# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='products_images/'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
