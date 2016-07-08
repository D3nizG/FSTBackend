# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0002_auto_20160708_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 8, 1, 13, 40, 210245), verbose_name=b'auto_now_add=true'),
        ),
    ]
