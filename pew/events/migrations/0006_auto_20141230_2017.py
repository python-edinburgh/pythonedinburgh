# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
