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
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=400)),
                ('story', models.TextField()),
                ('image_url', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime(2016, 7, 15, 2, 18, 40, 415003), verbose_name=b'auto_now_add=true', editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 2, 18, 40, 411481), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
