# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbs_view', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kbs_document',
            name='publisher',
            field=models.CharField(default='Steven Stapler', max_length=50),
        ),
    ]