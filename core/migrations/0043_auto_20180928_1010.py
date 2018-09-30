# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_watches_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='core.CartItem'),
        ),
        migrations.AlterField(
            model_name='watches',
            name='gender',
            field=models.CharField(choices=[('M', 'Men'), ('W', 'Women'), ('U', 'Unisex')], max_length=1, null=True),
        ),
    ]