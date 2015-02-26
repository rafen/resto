# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20150225_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='identifier',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
    ]
