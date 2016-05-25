# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osAnuncios', '0004_auto_20160123_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaveImagens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner', models.FileField(upload_to=b'Banner/')),
                ('piloto', models.FileField(upload_to=b'Piloto/')),
                ('fotoMo', models.FileField(upload_to=b'FotosModel/')),
                ('fotoCE', models.FileField(upload_to=b'FotosCenas/')),
            ],
        ),
        migrations.RemoveField(
            model_name='nave',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='nave',
            name='fotoCE',
        ),
        migrations.RemoveField(
            model_name='nave',
            name='fotoMo',
        ),
        migrations.RemoveField(
            model_name='nave',
            name='piloto',
        ),
        migrations.AddField(
            model_name='naveimagens',
            name='nave',
            field=models.ForeignKey(to='osAnuncios.Nave'),
        ),
    ]
