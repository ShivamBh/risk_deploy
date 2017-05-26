# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_reportloc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportloc',
            name='latitude',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
        migrations.AlterField(
            model_name='reportloc',
            name='longitude',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
    ]
