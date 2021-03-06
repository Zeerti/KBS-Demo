# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbs_view', '0007_files_upload_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='software_product',
            field=models.CharField(choices=[('BR', 'Brink'), ('PX', 'Pixel'), ('SV', 'Siva'), ('HR', 'Heritage')], default='BR', help_text='Select the software regarding this KBS Document', max_length=2, verbose_name='Software Product'),
        ),
        migrations.AlterField(
            model_name='document',
            name='body',
            field=models.TextField(help_text='Enter the detailed information for this KBS Document'),
        ),
        migrations.AlterField(
            model_name='document',
            name='favorited',
            field=models.BooleanField(default=False, editable=False, verbose_name='Favorited?'),
        ),
        migrations.AlterField(
            model_name='document',
            name='publisher',
            field=models.CharField(default='Zoidberg', max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=128, unique=True, verbose_name='Document Title'),
        ),
        migrations.AlterField(
            model_name='document',
            name='views',
            field=models.IntegerField(default=0, editable=False, help_text='Number of times this document has been viewed.'),
        ),
    ]
