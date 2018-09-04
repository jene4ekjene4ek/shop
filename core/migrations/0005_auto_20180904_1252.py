# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180904_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='watches',
            name='char',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='watches',
            name='image',
            field=models.ImageField(default=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='watches',
            name='sex',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AddField(
            model_name='watches',
            name='slug',
            field=models.SlugField(default=True),
        ),
    ]