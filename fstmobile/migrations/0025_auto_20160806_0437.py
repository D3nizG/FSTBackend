# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0024_auto_20160803_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=b'None', max_length=255),
        ),
        migrations.AddField(
            model_name='news',
            name='news_url',
            field=models.CharField(default=b'None', max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 6, 4, 37, 47, 589198, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
