# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_restaurant_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='rating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
