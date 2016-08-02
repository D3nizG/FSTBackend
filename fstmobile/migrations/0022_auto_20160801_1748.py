# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0021_auto_20160801_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created',
        ),
        migrations.RemoveField(
            model_name='scholarship',
            name='created',
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 17, 48, 28, 133844, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
