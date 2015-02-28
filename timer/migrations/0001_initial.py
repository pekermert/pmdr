# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'DV', max_length=2, choices=[(b'TL', b'Team Lead'), (b'DV', b'Developer'), (b'SM', b'Scrum Master')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('name', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('corp', models.ForeignKey(to='timer.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('types', models.CharField(default=b'ST', max_length=2, choices=[(b'ST', b'Study Time'), (b'SB', b'Short break'), (b'LB', b'Long break')])),
                ('status', models.CharField(default=b'CT', max_length=2, choices=[(b'DN', b'Done Pmdr'), (b'CL', b'Canceled Pmdr'), (b'CT', b'Still continues')])),
                ('team', models.ForeignKey(to='timer.Teams')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75, serialize=False, primary_key=True)),
                ('passwd', models.CharField(max_length=100)),
                ('groups', models.ForeignKey(to='timer.Groups')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='timerecord',
            name='user',
            field=models.ForeignKey(to='timer.Users'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='timerecord',
            unique_together=set([('user', 'start_time')]),
        ),
        migrations.AlterUniqueTogether(
            name='teams',
            unique_together=set([('name', 'corp')]),
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(to='timer.Users'),
            preserve_default=True,
        ),
    ]
