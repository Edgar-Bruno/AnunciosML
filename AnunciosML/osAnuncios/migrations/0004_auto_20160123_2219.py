# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osAnuncios', '0003_auto_20160108_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afiliacao',
            name='afiliacao',
            field=models.CharField(max_length=40),
        ),
    ]
