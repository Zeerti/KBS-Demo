# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 03:41
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('kbs_view', '0009_document_testbody'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='testBody',
        ),
        migrations.AlterField(
            model_name='document',
            name='body',
            field=markdownx.models.MarkdownxField(help_text='Enter the detailed information for this KBS Document'),
        ),
    ]