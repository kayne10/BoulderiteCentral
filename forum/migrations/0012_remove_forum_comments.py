# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-09-22 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_remove_forum_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='comments',
        ),
    ]
