# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0008_auto_20150527_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judgingtable',
            name='officials',
        ),
    ]
