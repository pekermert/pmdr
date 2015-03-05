# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('types', models.CharField(default=b'ST', max_length=2, choices=[(b'ST', b'Study Time'), (b'SB', b'Short break'), (b'LB', b'Long break')])),
                ('status', models.CharField(default=b'CT', max_length=2, choices=[(b'DN', b'Done'), (b'CL', b'Canceled'), (b'CT', b'Contuniues')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
