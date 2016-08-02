# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0015_auto_20160801_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='num_of_awards',
            field=models.CharField(default=b'None', max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 16, 16, 52, 347657), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 16, 16, 52, 349834), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 1, 16, 16, 52, 351273), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
