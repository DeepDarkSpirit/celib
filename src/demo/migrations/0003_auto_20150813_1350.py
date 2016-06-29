# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_tbook_tloaninfo_tuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateField(),
        ),
    ]
