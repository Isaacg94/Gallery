# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-11 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='gallery/'),
            preserve_default=False,
        ),
    ]
