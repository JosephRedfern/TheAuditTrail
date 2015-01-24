# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0005_auto_20150124_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='user',
            field=models.ForeignKey(null=True, default=None, blank=True, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
