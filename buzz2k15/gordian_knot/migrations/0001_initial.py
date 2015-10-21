# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.IntegerField()),
                ('time_submitted', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'time submitted')),
                ('correct', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.TextField(max_length=1000, verbose_name=b'Question')),
                ('level', models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('correct_answer', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='gordian_knot.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
