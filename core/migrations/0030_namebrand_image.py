# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20180919_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='namebrand',
            name='image',
            field=models.ImageField(default=True, upload_to='img'),
        ),
    ]
