# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-15 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_watches_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watches',
            name='slug',
            field=models.SlugField(default=True),
        ),
    ]
