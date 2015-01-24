# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_auto_20150124_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='data',
            new_name='date',
        ),
    ]
