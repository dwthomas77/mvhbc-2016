# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JudgingTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('session', models.CharField(default=b'AM', max_length=200, blank=True)),
                ('locked', models.BooleanField(default=False)),
                ('officials', models.ForeignKey(to='competition.UserProfile', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('competition_id', models.CharField(max_length=20, blank=True)),
                ('paid', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('comments', models.TextField(blank=True)),
                ('check_in', models.DateField(blank=True)),
                ('received', models.DateField(blank=True)),
                ('score', models.CharField(max_length=20, blank=True)),
                ('place', models.CharField(max_length=200, blank=True)),
                ('brewer', models.ForeignKey(to='competition.UserProfile', blank=True)),
                ('style', models.ForeignKey(to='competition.Style', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='style',
            name='table',
            field=models.ForeignKey(blank=True, to='competition.JudgingTable', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='qualification',
            field=models.CharField(default=b'Apprentice', max_length=200, blank=True, choices=[(b'Apprentice', b'Apprentice'), (b'Certified', b'Certified'), (b'Recognized', b'Recognized'), (b'National', b'National'), (b'Master', b'Master'), (b'Grand Master', b'Grand Master'), (b'Professional Brewer', b'Professional Brewer')]),
        ),
    ]
