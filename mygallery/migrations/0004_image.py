# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-10 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0003_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=30)),
                ('img_description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygallery.Category')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygallery.Editor')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygallery.Location')),
            ],
        ),
    ]
