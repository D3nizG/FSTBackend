# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0025_auto_20160806_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='website',
            field=models.CharField(default=b'None', max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 6, 5, 45, 26, 758187, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
