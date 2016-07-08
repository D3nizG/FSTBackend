# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
