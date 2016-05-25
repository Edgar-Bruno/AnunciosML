# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osAnuncios', '0002_remove_nave_produzido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estoque',
            old_name='flag',
            new_name='flat',
        ),
    ]
