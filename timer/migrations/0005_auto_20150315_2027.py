# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0004_auto_20150305_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authtoken',
            name='user',
        ),
        migrations.DeleteModel(
            name='AuthToken',
        ),
        migrations.RemoveField(
            model_name='timerecord',
            name='on_time',
        ),
        migrations.AlterField(
            model_name='timerecord',
            name='on_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
