# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='When',
            field=models.DateTimeField(default=timezone.datetime(2014, 12, 30, 12, 11, 52, 289837, tzinfo=utc), verbose_name='When is the event?'),
            preserve_default=False,
        ),
    ]
