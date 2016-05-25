# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

#Produto

class Produtor(models.Model):
	nomeProdutor = models.CharField(max_length=20, blank = False, null = False)
	fotoPR = models.FileField(upload_to="Produtor/")

	def __unicode__(self):
		return self.nomeProdutor

class Produto(models.Model):
	produtoNome = models.CharField(max_length=30, blank = True, null = True)
	dataEntrada = models.DateTimeField(auto_now_add=False, auto_now=True)
	produzido = models.ForeignKey(Produtor)
	
	def __unicode__(self):
		return self.produtoNome

# Naves StarWars
class Afiliacao(models.Model):
	afiliacao = models.CharField(max_length=40, blank = False, null = False)
	fotoAF = models.FileField(upload_to="Afiliacao/")

	def __unicode__(self):
		return self.afiliacao

class Poster(models.Model):
	posterIMG =	models.FileField(upload_to="Poster/", help_text="Escolha a imagem para o poster")
	subtitulos = models.CharField(
		help_text="Coloque o subtitulo do filme",
		max_length=50, blank = False, null = False)
	lancamento = models.DateField('Data de Lançamento',
		help_text="Coloque a data de lançamento")
	detalhe = models.CharField(max_length=136, blank = False, null = False)

	def __unicode__(self):
		return self.subtitulos

class Cores(models.Model):
	coresNom = models.CharField(max_length=10, blank = False, null = False)
	coresHex = models.CharField(max_length=7, blank = False, null = False)
	
	def __unicode__(self):
		return self.coresNom

	def getHex(self):
		return self.coresHex

class Caracteristica(models.Model):
	caracteristica = models.CharField(max_length = 30, blank = False, null = True)	
	def __unicode__(self):
		return self.caracteristica

class Fabricante(models.Model):
	fabricante = models.CharField(max_length = 50, blank = False, null = False)	
	def __unicode__(self):
		return self.fabricante

class Nave(models.Model):
	pud_date = models.DateTimeField('Data de Publicação', auto_now_add=True)
	naveNome = models.CharField(max_length=30, blank = False, null = False)
	nomepiloto = models.CharField(max_length=30, blank = False, null = False)
	produto = models.OneToOneField(Produto)
	poster = models.ForeignKey(Poster)
	cores = models.ForeignKey(Cores)
	afiliacao = models.ForeignKey(Afiliacao)
	fabricante = models.ForeignKey(Fabricante)

	def __unicode__(self):
		return self.naveNome

	def get_naveNome(self):
		return self.naveNome.replace('\'', '--').replace(' ', '_')

	def get_next_preview_by_afiliacao(self):
		
		objPrevNext = Nave.objects.select_related().filter(afiliacao_id=self.afiliacao_id).order_by('naveNome')

		atual = False
		naveNext = None
		navePrev = None
	
		for i in objPrevNext:
			
			if atual:
				naveNext = i.naveNome
				break

			if i.id == self.id:
				atual = True
				continue

			navePrev = i.naveNome

		return (navePrev, naveNext)



class NaveImagens(models.Model):
	nave = models.ForeignKey(Nave, related_name='imagensN')
	banner	= models.FileField(upload_to="Banner/", default=False)
	piloto	= models.FileField(upload_to="Piloto/", default=False)
	fotoMo = models.FileField(upload_to="FotosModel/", default=False)
	fotoCE = models.FileField(upload_to="FotosCenas/", default=False)

	def __unicode__(self):
		return self.banner

class Descricao(models.Model):
	nave = models.ForeignKey(Nave)
	caracteristica = models.ForeignKey(Caracteristica)
	informacao = models.TextField(max_length=500, blank=True, null=True)

	def __unicode__(self):
		return self.informacao

class FotosAnuncio(models.Model):
	nave = models.ForeignKey(Nave)
	fotoAN = models.FileField(upload_to="FotosAnuncio/")

class FasciculosLista(models.Model):
	fasciculo = models.CharField(max_length=50)
	def __unicode__(self):
		return self.fasciculo
 
class ItemCaracteristica(models.Model):

	nave = models.ForeignKey(Nave)
	dimecoes = models.CharField(max_length=20, blank=True, null=False, default=0)
	revista = models.CharField(max_length=10, blank=True, null=False, default=0)
	extras = models.CharField(max_length=50, blank=True, null=True)
	fasciculo = models.ForeignKey(FasciculosLista)

#Estoque

class Estoque(models.Model):
	produto = models.ForeignKey(Produto)
	atualizAtual = models.DateTimeField(auto_now_add=False, auto_now=True)
	atualizEntrada = models.DateTimeField(auto_now_add=True, auto_now=False)
	estoqAtual = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
	estoqEntrada = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
	valorUni = models.DecimalField(max_digits=5, decimal_places=2)
	flat = models.BooleanField(default=True)

	def __unicode__(self):
		return self.estoqAtual

class Venda(models.Model):
	produto = models.ForeignKey(Produto)
	estoque = models.ForeignKey(Estoque) 
	dataVenda = models.DateTimeField(auto_now_add=False, auto_now=True)
	quantidadeVenda = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
	valorVenda = models.DecimalField(max_digits=5, decimal_places=2)