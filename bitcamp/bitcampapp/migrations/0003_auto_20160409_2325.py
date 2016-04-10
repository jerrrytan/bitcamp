# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcampapp', '0002_meal_meal_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_cost',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
