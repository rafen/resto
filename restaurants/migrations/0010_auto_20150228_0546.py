# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_restaurant_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
