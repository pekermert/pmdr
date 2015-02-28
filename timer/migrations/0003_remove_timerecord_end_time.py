# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0002_auto_20150222_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timerecord',
            name='end_time',
        ),
    ]
