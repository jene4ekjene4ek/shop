# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20180918_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watches',
            name='namebrand_id',
        ),
    ]