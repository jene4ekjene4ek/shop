# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-30 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20180930_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderposition',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderposition',
            name='watches',
        ),
        migrations.AlterField(
            model_name='watches',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Men'), (1, 'Women'), (2, 'Unisex')], null=True),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderPosition',
        ),
    ]
