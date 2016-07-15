# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0010_auto_20160715_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=255)),
                ('shortname', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 3, 27, 33, 411147), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 3, 27, 33, 419117), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 3, 27, 33, 426930), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
