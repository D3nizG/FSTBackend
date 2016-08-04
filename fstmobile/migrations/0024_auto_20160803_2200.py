# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0023_auto_20160801_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 3, 22, 0, 25, 617527, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.CharField(max_length=300),
        ),
    ]
