# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 03:29
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('kbs_view', '0008_auto_20170327_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='testBody',
            field=markdownx.models.MarkdownxField(default=''),
        ),
    ]
