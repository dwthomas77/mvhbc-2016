# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0009_remove_judgingtable_officials'),
    ]

    operations = [
        migrations.AddField(
            model_name='judgingtable',
            name='judges',
            field=models.ManyToManyField(related_name=b'judges', to='competition.UserProfile'),
            preserve_default=True,
        ),
    ]
