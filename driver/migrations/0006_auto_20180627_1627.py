# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0005_auto_20180626_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_images/default_image.png', upload_to='profile_images/'),
        ),
    ]
