# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0004_auto_20150124_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]