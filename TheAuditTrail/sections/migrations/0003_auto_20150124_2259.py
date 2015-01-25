# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_section_bounding_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='index',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
