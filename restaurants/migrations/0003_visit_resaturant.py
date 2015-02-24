# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='resaturant',
            field=models.ForeignKey(default=None, to='restaurants.Restaurant'),
            preserve_default=False,
        ),
    ]
