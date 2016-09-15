# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0048_auto_20160915_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 16, 52, 35, 62993, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 16, 52, 35, 57636, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
