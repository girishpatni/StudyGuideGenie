# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20160416_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default='12345', max_length=120),
        ),
    ]
