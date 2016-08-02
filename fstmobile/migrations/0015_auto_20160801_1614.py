# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0014_auto_20160730_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarship',
            name='detail',
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 16, 14, 24, 344897), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 16, 14, 24, 346835), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 16, 14, 24, 347682), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
