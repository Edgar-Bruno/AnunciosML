# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osAnuncios', '0006_auto_20160224_2300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poster',
            old_name='poster',
            new_name='posterIMG',
        ),
        migrations.AlterField(
            model_name='poster',
            name='detalhe',
            field=models.CharField(default=1, max_length=136),
            preserve_default=False,
        ),
    ]
