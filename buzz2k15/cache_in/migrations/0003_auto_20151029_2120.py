# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cache_in', '0002_question_q_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_image2',
            field=models.ImageField(upload_to=b'cache_in_images', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image3',
            field=models.ImageField(upload_to=b'cache_in_images', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image4',
            field=models.ImageField(upload_to=b'cache_in_images', blank=True),
        ),
    ]
