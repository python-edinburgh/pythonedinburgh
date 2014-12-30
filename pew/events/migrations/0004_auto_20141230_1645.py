# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20141230_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_dt']},
        ),
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
