# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 08:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0033_auto_20160820_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 26, 8, 14, 56, 463450, tzinfo=utc), editable=False, verbose_name=b'auto_now_add=true'),
        ),
    ]