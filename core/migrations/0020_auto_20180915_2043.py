# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-15 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20180915_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='BrandName',
        ),
    ]
