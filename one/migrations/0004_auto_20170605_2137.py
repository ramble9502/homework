# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0003_auto_20170605_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewwine',
            name='content',
            field=models.TextField(max_length=2000),
        ),
    ]
