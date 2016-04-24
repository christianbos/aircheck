# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temperature',
            name='celcius',
        ),
        migrations.AddField(
            model_name='temperature',
            name='celsius',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='gas',
            name='ppm',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='rangomed',
            field=models.FloatField(blank=True, max_length=950, null=True),
        ),
    ]
