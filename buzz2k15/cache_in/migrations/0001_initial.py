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
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('question_number', models.IntegerField(default=0)),
                ('time_completed', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(related_name='CacheIn_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_image1', models.ImageField(upload_to=b'cache_in_images')),
                ('question_image2', models.ImageField(upload_to=b'cache_in_images')),
                ('question_image3', models.ImageField(upload_to=b'cache_in_images')),
                ('question_image4', models.ImageField(upload_to=b'cache_in_images')),
                ('answer', models.CharField(max_length=1000)),
            ],
        ),
    ]
