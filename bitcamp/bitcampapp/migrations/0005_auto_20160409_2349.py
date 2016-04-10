# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcampapp', '0004_auto_20160409_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_cost',
            field=models.IntegerField(default=10),
        ),
    ]
