# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0009_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=400)),
                ('detail', models.TextField()),
                ('image_url', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime(2016, 7, 15, 3, 1, 51, 235959), verbose_name=b'auto_now_add=true', editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 3, 1, 51, 227967), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 3, 1, 51, 233018), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
