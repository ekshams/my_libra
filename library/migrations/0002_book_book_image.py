# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.FileField(default=None, upload_to=b''),
        ),
    ]