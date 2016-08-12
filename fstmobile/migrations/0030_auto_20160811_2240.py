# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0029_auto_20160808_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 11, 22, 40, 46, 944366, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.CharField(max_length=600),
        ),
    ]
