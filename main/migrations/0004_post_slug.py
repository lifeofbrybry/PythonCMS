# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160101_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, verbose_name=b'slug'),
        ),
    ]