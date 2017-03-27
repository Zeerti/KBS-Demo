# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbs_view', '0008_document_software_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='body',
            field=models.TextField(help_text='Enter the detailed information for this KBS Document'),
        ),
        migrations.AlterField(
            model_name='document',
            name='publisher',
            field=models.CharField(default='Zoidberg', max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='software_product',
            field=models.CharField(choices=[('BR', 'Brink'), ('PX', 'Pixel'), ('SV', 'Siva'), ('HR', 'Heritage')], default='BR', help_text='Select the software regarding this KBS Document', max_length=2),
        ),
        migrations.AlterField(
            model_name='document',
            name='views',
            field=models.IntegerField(default=0, help_text='Number of times this document has been viewed.'),
        ),
    ]