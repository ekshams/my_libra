# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20170122_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_image',
        ),
    ]
