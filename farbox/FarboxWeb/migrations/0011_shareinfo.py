# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarboxWeb', '0010_auto_20160605_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareInfo',
            fields=[
                ('share_key', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('path_id', models.IntegerField()),
            ],
        ),
    ]
