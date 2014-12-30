# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_when'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='When',
            new_name='event_dt',
        ),
    ]
