# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0007_auto_20160708_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 11, 19, 17, 48, 112321), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
