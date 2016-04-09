# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0010_judgingtable_judges'),
    ]

    operations = [
        migrations.AddField(
            model_name='judgingtable',
            name='stewards',
            field=models.ManyToManyField(related_name=b'stewards', to='competition.UserProfile'),
            preserve_default=True,
        ),
    ]
