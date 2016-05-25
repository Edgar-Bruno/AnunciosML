# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('afiliacao', models.CharField(max_length=20)),
                ('fotoAF', models.FileField(upload_to=b'Afiliacao/')),
            ],
        ),
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caracteristica', models.CharField(max_length=30, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coresNom', models.CharField(max_length=10)),
                ('coresHex', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Descricao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('informacao', models.TextField(max_length=500, null=True, blank=True)),
                ('caracteristica', models.ForeignKey(to='osAnuncios.Caracteristica')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atualizAtual', models.DateTimeField(auto_now=True)),
                ('atualizEntrada', models.DateTimeField(auto_now_add=True)),
                ('estoqAtual', models.PositiveSmallIntegerField(default=0)),
                ('estoqEntrada', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('valorUni', models.DecimalField(max_digits=5, decimal_places=2)),
                ('flag', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fabricante', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FasciculosLista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fasciculo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FotosAnuncio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fotoAN', models.FileField(upload_to=b'FotosAnuncio/')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCaracteristica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dimecoes', models.CharField(default=0, max_length=20, blank=True)),
                ('revista', models.CharField(default=0, max_length=10, blank=True)),
                ('extras', models.CharField(max_length=50, null=True, blank=True)),
                ('fasciculo', models.ForeignKey(to='osAnuncios.FasciculosLista')),
            ],
        ),
        migrations.CreateModel(
            name='Nave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pud_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Data de Publica\xc3\xa7\xc3\xa3o')),
                ('naveNome', models.CharField(max_length=30)),
                ('banner', models.FileField(upload_to=b'Banner/')),
                ('piloto', models.FileField(upload_to=b'Piloto/')),
                ('nomepiloto', models.CharField(max_length=30)),
                ('fotoMo', models.FileField(upload_to=b'FotosModel/')),
                ('fotoCE', models.FileField(upload_to=b'FotosCenas/')),
                ('afiliacao', models.ForeignKey(to='osAnuncios.Afiliacao')),
                ('cores', models.ForeignKey(to='osAnuncios.Cores')),
                ('fabricante', models.ForeignKey(to='osAnuncios.Fabricante')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poster', models.FileField(help_text=b'Escolha a imagem para o poster', upload_to=b'Poster/')),
                ('subtitulos', models.CharField(help_text=b'Coloque o subtitulo do filme', max_length=50)),
                ('lancamento', models.DateField(help_text=b'Coloque a data de lan\xc3\xa7amento', verbose_name=b'Data de Lan\xc3\xa7amento')),
                ('detalhe', models.CharField(max_length=136, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('produtoNome', models.CharField(max_length=30, null=True, blank=True)),
                ('dataEntrada', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeProdutor', models.CharField(max_length=20)),
                ('fotoPR', models.FileField(upload_to=b'Produtor/')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataVenda', models.DateTimeField(auto_now=True)),
                ('quantidadeVenda', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('valorVenda', models.DecimalField(max_digits=5, decimal_places=2)),
                ('estoque', models.ForeignKey(to='osAnuncios.Estoque')),
                ('produto', models.ForeignKey(to='osAnuncios.Produto')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='produzido',
            field=models.ForeignKey(to='osAnuncios.Produtor'),
        ),
        migrations.AddField(
            model_name='nave',
            name='poster',
            field=models.ForeignKey(to='osAnuncios.Poster'),
        ),
        migrations.AddField(
            model_name='nave',
            name='produto',
            field=models.OneToOneField(to='osAnuncios.Produto'),
        ),
        migrations.AddField(
            model_name='nave',
            name='produzido',
            field=models.ForeignKey(to='osAnuncios.Produtor'),
        ),
        migrations.AddField(
            model_name='itemcaracteristica',
            name='nave',
            field=models.ForeignKey(to='osAnuncios.Nave'),
        ),
        migrations.AddField(
            model_name='fotosanuncio',
            name='nave',
            field=models.ForeignKey(to='osAnuncios.Nave'),
        ),
        migrations.AddField(
            model_name='estoque',
            name='produto',
            field=models.ForeignKey(to='osAnuncios.Produto'),
        ),
        migrations.AddField(
            model_name='descricao',
            name='nave',
            field=models.ForeignKey(to='osAnuncios.Nave'),
        ),
    ]
