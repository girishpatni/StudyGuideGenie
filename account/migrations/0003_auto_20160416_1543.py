# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 22:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160416_1525'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserForm',
            new_name='UserProfile',
        ),
    ]
