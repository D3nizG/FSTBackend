# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0019_auto_20160801_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='created',
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 17, 41, 24, 487970), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 17, 41, 24, 490901), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
