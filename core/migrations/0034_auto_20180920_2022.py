# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20180920_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namebrand',
            name='image',
            field=models.ImageField(default=True, upload_to='img'),
        ),
    ]
