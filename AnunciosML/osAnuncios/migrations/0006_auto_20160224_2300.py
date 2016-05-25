# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osAnuncios', '0005_auto_20160215_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naveimagens',
            name='nave',
            field=models.ForeignKey(related_name='imagensN', to='osAnuncios.Nave'),
        ),
    ]
