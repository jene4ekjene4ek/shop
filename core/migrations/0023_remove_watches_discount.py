# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-15 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_watches_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watches',
            name='discount',
        ),
    ]
