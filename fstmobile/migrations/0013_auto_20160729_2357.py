# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0012_auto_20160729_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=400)),
                ('detail', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2016, 7, 29, 23, 57, 4, 348496), verbose_name=b'auto_now_add=true', editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 29, 23, 57, 4, 344990), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 29, 23, 57, 4, 347469), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
