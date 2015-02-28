# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='groups',
            field=models.CharField(default=b'DV', max_length=2, choices=[(b'TL', b'Team Lead'), (b'DV', b'Developer'), (b'SM', b'Scrum Master')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
    ]
