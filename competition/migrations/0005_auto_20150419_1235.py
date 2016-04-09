# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0004_userprofile_judge_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='judge_preference',
            field=models.CharField(default=b'None', max_length=200, choices=[(b'None', b'None'), (b'Steward', b'Steward'), (b'Judge', b'Judge')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='aha_id',
            field=models.CharField(max_length=200, verbose_name=b'AHA ID', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bjcp_registration',
            field=models.CharField(max_length=100, verbose_name=b'BJCP Registration ID', blank=True),
        ),
    ]
