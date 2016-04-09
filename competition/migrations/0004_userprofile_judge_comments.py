# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_auto_20150418_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='judge_comments',
            field=models.TextField(null=True, verbose_name=b'Comments/Special Reqeusts', blank=True),
            preserve_default=True,
        ),
    ]
