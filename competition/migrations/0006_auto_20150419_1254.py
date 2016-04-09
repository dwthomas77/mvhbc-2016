# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0005_auto_20150419_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='judge_preference',
            field=models.CharField(default=b'None', max_length=200, blank=True, choices=[(b'None', b'None'), (b'Steward', b'Steward'), (b'Judge', b'Judge')]),
        ),
    ]
