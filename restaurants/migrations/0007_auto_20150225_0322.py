# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20150224_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='telephone',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='website',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
