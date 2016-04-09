# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0007_auto_20150509_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='judge_preference',
            field=models.CharField(default=b'None', max_length=200, blank=True, choices=[(b'None', b'.....'), (b'Steward', b'Steward'), (b'Judge', b'Judge')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='qualification',
            field=models.CharField(default=b'None', max_length=200, blank=True, choices=[(b'None', b'.....'), (b'Apprentice', b'Apprentice'), (b'Certified', b'Certified'), (b'Recognized', b'Recognized'), (b'National', b'National'), (b'Master', b'Master'), (b'Grand Master', b'Grand Master'), (b'Professional Brewer', b'Professional Brewer')]),
        ),
    ]
