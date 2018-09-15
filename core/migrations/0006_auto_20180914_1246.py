# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180904_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watches',
            name='sex',
        ),
        migrations.AddField(
            model_name='watches',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Unisex')], null=True),
        ),
        migrations.AlterField(
            model_name='watches',
            name='date_add',
            field=models.DateField(),
        ),
    ]
