# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sections', '0003_auto_20150124_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='section',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.AddField(
            model_name='section',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
    ]
