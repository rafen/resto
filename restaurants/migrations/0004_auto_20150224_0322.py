# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_visit_resaturant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='resaturant',
            new_name='restaurant',
        ),
    ]
