# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0006_auto_20150419_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='check_in',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='received',
            field=models.DateField(null=True, blank=True),
        ),
    ]
