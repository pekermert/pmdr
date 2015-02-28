# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0003_remove_timerecord_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timerecord',
            name='status',
            field=models.CharField(default=b'CT', max_length=2, choices=[(b'DN', b'Done'), (b'CL', b'Canceled'), (b'CT', b'Contuniues')]),
            preserve_default=True,
        ),
    ]
