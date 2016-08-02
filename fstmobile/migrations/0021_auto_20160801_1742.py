# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0020_auto_20160801_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 17, 42, 19, 767632, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 17, 42, 19, 765068), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 17, 42, 19, 769071), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
