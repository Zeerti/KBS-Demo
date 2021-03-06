# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kbs_view', '0003_auto_20170321_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='')),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='file',
        ),
        migrations.RemoveField(
            model_name='document',
            name='image',
        ),
        migrations.AddField(
            model_name='files',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kbs_view.Document'),
        ),
    ]
