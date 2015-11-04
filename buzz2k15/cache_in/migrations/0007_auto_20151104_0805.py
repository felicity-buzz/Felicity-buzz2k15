# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache_in', '0006_auto_20151030_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_image2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_image3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_image4',
        ),
    ]
