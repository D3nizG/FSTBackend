# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0042_auto_20160830_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 9, 14, 4, 21, 7, 560323, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 4, 21, 7, 555134, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
