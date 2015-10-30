# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cache_in', '0005_auto_20151030_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='solved',
            field=models.CharField(default=b'0,', max_length=300, blank=True),
        ),
    ]
