# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeTable_app', '0003_auto_20160210_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='code_lang',
            field=models.CharField(default='xx', max_length=10),
        ),
        migrations.AddField(
            model_name='code',
            name='run_count',
            field=models.IntegerField(default=0),
        ),
    ]
