# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0018_auto_20160801_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='application_url',
            field=models.CharField(default=b'None', max_length=400),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 17, 35, 45, 7740), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 17, 35, 45, 11012), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 17, 35, 45, 12505), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
