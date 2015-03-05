# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timerecord',
            old_name='date',
            new_name='on_date',
        ),
        migrations.RenameField(
            model_name='timerecord',
            old_name='time',
            new_name='on_time',
        ),
        migrations.RenameField(
            model_name='timerecord',
            old_name='user',
            new_name='owner',
        ),
    ]
