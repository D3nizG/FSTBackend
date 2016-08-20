# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0032_auto_20160820_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 20, 22, 33, 48, 557014, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
