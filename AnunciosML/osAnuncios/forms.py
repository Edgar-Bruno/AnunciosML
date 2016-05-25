# -*- coding: utf-8 -*-
from django.forms.extras.widgets import SelectDateWidget
from dal import autocomplete
from django import forms
from django.forms.util import ErrorList

import hashlib

from django.forms import formsets

from osAnuncios.models import *

class afiliacaoForms(forms.ModelForm):

	val = hashlib.sha512("Afiliacao")
	arg = val.hexdigest()
	val = hashlib.sha512("afiliacao")
	argb = val.hexdigest()

	afiliacaoADD = forms.CharField(widget=forms.TextInput(attrs={'placeholder'	: u'Digite a nova afiliação'
																,'size'			: '35'
																,'onclick' 		: "AutoComplete(this.id, '%s', '%s');" % (arg, argb)}))

	# Regra para validar a adição de uma nova Afiliação
	checkBox_afiliacao = forms.BooleanField(initial=False, required=False)

	fotoAF = forms.FileField(   label="Bandeira da Afiliação",
								required=True,
								widget=forms.ClearableFileInput(attrs={
									'onclick' 	:"ImageChange(this);",
									'accept'	:'image/*',
									'class'		:'inputFILE'})
							)

	class Meta:
			
		model = Afiliacao

		fields = ['afiliacao', 'fotoAF']

		labels  = {
			'afiliacao'		: "Escolha a Afiliação."
		}

		widgets = {
			'afiliacao'		:	forms.TextInput(attrs={'placeholder'	: u'Digite a afiliação','size': '35'}),

        }

	def __init__(self, *args, **kwargs):
		super(afiliacaoForms, self).__init__(*args, **kwargs)

		self.fields['checkBox_afiliacao'].widget.attrs['class'] = 'checkBoxADD'

	def salveValueADD(self, obj_afiliacao):

		addAfili = Afiliacao(
				afiliacao = obj_afiliacao['afiliacaoADD'].value(),
				fotoAF = obj_afiliacao['fotoAF'].value()
		)

		if not Afiliacao.objects.filter(afiliacao=addAfili.afiliacao):		

			addAfili.save()
			return addAfili

		else:

			return obj_afiliacao.add_error('afiliacaoADD', u'Adicione uma outra pois, [ %s ] já existe' % addAfili.afiliacao)

	
	def clean_afiliacao(self):

		afiliacao = self.cleaned_data.get('afiliacao')

		if Afiliacao.objects.filter(afiliacao=afiliacao):
			raise forms.ValidationError(u'Essa afiliação [ %s ] já existe' % afiliacao)
		return afiliacao

class CaracteristicaForms(forms.ModelForm):

	class Meta:
		model = Caracteristica
		fields = ['caracteristica']

	
	def clean_caracteristica(self):
		caracteristica = self.cleaned_data.get('caracteristica')
				
		if Caracteristica.objects.filter(caracteristica=caracteristica):
			raise forms.ValidationError(u'Essa caracteristica [ %s ] já existe' % caracteristica)
		return caracteristica


class fabricanteForms(forms.ModelForm):

	val = hashlib.sha512("Fabricante")
	arg = val.hexdigest()
	val = hashlib.sha512("fabricante")
	argb = val.hexdigest()

	fabricanteADD = forms.CharField(widget=forms.TextInput(attrs={'placeholder'	: u'Digite um novo fabricante'
																,'size'			: '35'
																,'onclick' 		: "AutoComplete(this.id, '%s', '%s');" % (arg, argb)}))

	# Regra para validar a adição de um novo fabricante
	checkBox_fabricante = forms.BooleanField(initial=False, required=False)

	class Meta:
		model = Fabricante
		fields = ['fabricante']
	
	def __init__(self, *args, **kwargs):
		super(fabricanteForms, self).__init__(*args, **kwargs)
		self.fields['checkBox_fabricante'].widget.attrs['class'] = 'checkBoxADD'

	def salveValueADD(self, obj_fabricante):


		addFabri = Fabricante(fabricante = obj_fabricante['fabricanteADD'].value())

		if not Fabricante.objects.filter(fabricante=addFabri.fabricante):		

			addFabri.save()
			return addFabri

		else:

			return obj_fabricante.add_error('fabricanteADD', u'Adicione uma outra pois, [ %s ] já existe' % addFabri.fabricante)
		
	def clean_fabricante(self):

		fabricante = self.cleaned_data.get('fabricante')

		if Fabricante.objects.filter(fabricante=fabricante):
			raise forms.ValidationError(u'Essa fabricante [ %s ] já existe' % fabricante)
		return fabricante

class DescricaoForms(forms.ModelForm):

	val = hashlib.sha512("Caracteristica")
	arg = val.hexdigest()
	val = hashlib.sha512("caracteristica")
	argb = val.hexdigest()


	caracteristicaADD = forms.CharField(required=False
									   ,widget=forms.TextInput(attrs={
											 'placeholder'	: u'Digite uma nova caracteristica'
											,'size'			: '35'
											,'onclick' 		: "AutoComplete(this.id, '%s', '%s');" % (arg, argb)}))

	checkBox_descricao = forms.BooleanField(initial=False, required=False)
	
	class Meta:

		model = Descricao
		
		fields = ['caracteristica', 'checkBox_descricao', 'caracteristicaADD', 'informacao']

		widgets = {
			'informacao'				: forms.Textarea(attrs={'placeholder'	: u'Digite a especificações da caracteristica.'
															   ,'cols'			: 35
															   ,'rows'			: 4})  
        }
	def __init__(self, *args, **kwargs):
		super(DescricaoForms, self).__init__(*args, **kwargs)

		self.fields['informacao'].widget.attrs['onkeydown'] = 'return textCounter(this, 200);'
		self.fields['informacao'].widget.attrs['onkeyup'] = 'return textCounter(this, 200);'
		self.fields['caracteristica'].queryset = Caracteristica.objects.all().order_by('caracteristica')
		self.fields['caracteristica'].empty_label = "Selecione"
		self.fields['caracteristica'].label = "Escolha uma Caracteristica"

		self.fields['checkBox_descricao'].widget.attrs['class'] = 'checkBoxADD'


	def salveValueADD(self, obj_item):

		if obj_item['checkBox_descricao'].value():

			addCaract = Caracteristica(caracteristica = obj_item['caracteristicaADD'].value())

			if not Caracteristica.objects.filter(caracteristica=addCaract.caracteristica):

				addCaract.save()

				#dic = { 'addCaract' : int(addCaract.id), 'checkBox_descricao': False } 	

				dic = { 'addCaract' : int(addCaract.id), 'error': None } 
				

			else:
				dic = { 'addCaract' : None, 'error': u'Adicione uma outra pois, [ %s ] já existe' % addCaract.caracteristica }
				
			return dic

	def clean_caracteristicaADD(self):

		caracteristicaADD = self.cleaned_data.get('caracteristicaADD')

		checkBox_descricao = self.cleaned_data.get('checkBox_descricao')

		if checkBox_descricao:
			if Caracteristica.objects.filter(caracteristica=caracteristicaADD):
				raise forms.ValidationError(u'Essa fabricante [ %s ] já existe' % caracteristicaADD)
			return caracteristicaADD

				

class coresForms(forms.ModelForm):

	checkBox_cores = forms.BooleanField(initial=False, required=False)

	class Meta:

		val = hashlib.sha512("Cores")
		arg = val.hexdigest()
		val = hashlib.sha512("coresNom")
		argb = val.hexdigest()

		model = Cores

		fields = ['coresNom', 'coresHex']

		help_text = {
			'coresNom'	: "Nome da cor",
			'coresHex'	: "Código em Hexadecimal"
		}


		labels = {
			'coresNom'	: 'Nome da cor',
			'coresHex'	: 'Código hexadecimal'
		}

		widgets = {

			'coresNom'	: forms.TextInput(attrs={'placeholder'	: u'Digite o nome da cor'
												,'size'			: '35'
												,'onclick' 		: "AutoComplete(this.id, '%s', '%s');" % (arg, argb)}),

			'coresHex'	: forms.TextInput(attrs={'type'			: 'color'
												,'help_text'	: 'Nome da cor'})
        }
        
	def __init__(self, *args, **kwargs):
		super(coresForms, self).__init__(*args, **kwargs)

		self.fields['checkBox_cores'].widget.attrs['class'] = 'checkBoxADD'

	def salveValueADD(self, objCor):

		addCor = Cores(
				coresNom = objCor['coresNom'].value(),
				coresHex = objCor['coresHex'].value()
		)

		if not Cores.objects.filter(coresNom=addCor.coresNom):		

			addCor.save()
			return addCor

		else:

			return objAfi.add_error('coresNom', u'Adicione uma outra pois, [ %s ] já existe' % addCor.coresNom)


class posterForms(forms.ModelForm):

	checkBox_poster = forms.BooleanField(initial=False, required=False)

	posterIMG = forms.FileField(	label="Escolha o poster do Filme",
									required=True,
									widget=forms.ClearableFileInput(attrs={
										'onclick' 	:"ImageChange(this);",
										'accept'	:'image/*',
										'class'		:'inputFILE'})
								)

	class Meta:

		val = hashlib.sha512("Poster")
		arg = val.hexdigest()
		val = hashlib.sha512("subtitulos")
		argb = val.hexdigest()

		model = Poster

		fields = ['subtitulos', 'lancamento', 'detalhe','posterIMG']

		widgets = {

			'lancamento'	: forms.TextInput(attrs={'placeholder'	 : u'Digite o nome da cor',
													  'id'      	 : 'datepicker',
													  'readonly'	 : True
													}),

			'detalhe'		: forms.Textarea(attrs={'placeholder': u'Digite uma breve descrição do filme',
													'cols'			: 45,
													'rows'			: 3,
													'onKeyDown' 	: 'return textCounter(this, 135);',
													'onkeyup'		: 'return textCounter(this, 135);'}),

			'subtitulos'    : forms.TextInput(attrs={'onclick' 		: "AutoComplete(this.id, '%s', '%s');" % (arg, argb)})
        }

	def __init__(self, *args, **kwargs):
		super(posterForms, self).__init__(*args, **kwargs)

		self.fields['checkBox_poster'].widget.attrs['class'] = 'checkBoxADD'

	def salveValueADD(self, objPoster):

		print "======================== salvePosterADD aqui"

		addPoster = Poster(
					posterIMG = objPoster['posterIMG'].value(),
					subtitulos = objPoster['subtitulos'].value(),
					lancamento = objPoster['lancamento'].value(),
					detalhe = objPoster['detalhe'].value()
				)

		if not Poster.objects.filter(subtitulos=addPoster.subtitulos):		

			addPoster.save()
			return addPoster

		else:

			return addPoster.add_error('subtitulos', u'Adicione uma outra pois, [ %s ] já existe' % addPoster.subtitulos)

class ItemCaracteristicaForms(forms.ModelForm):

    PRIORITY = (
		    (0, 'Selecione a revista'),
		    ('SIM', 'SIM'),
		    ('NÃO',	'NÃO'),
    )

    PRIORITYb = (
    		(0, 'Selecione a Dimenções'),
		    ('8,1x11,8x8,9 cm', '8,1x11,8x8,9 cm'),
		    ('9,6x13,1x8,9 cm', '9,6x13,1x8,9 cm'),
    )

    revista =  forms.ChoiceField(label = "Selecione a revista",
    							  choices=PRIORITY)

    dimecoes =  forms.ChoiceField(label = "Selecione a Dimenções",
    							  required=True,
    							  choices=PRIORITYb)


    class Meta:

		model = ItemCaracteristica

		fields = ['dimecoes', 'revista', 'fasciculo', 'extras']

		labels = {
			'dimecoes'		: "Dimenções",
			'revista'		: "Acompanha revista",
			'fasciculo'		: "Numero da edição",
		}

    def __init__(self, *args, **kwargs):
		super(ItemCaracteristicaForms, self).__init__(*args, **kwargs)
		self.fields['fasciculo'].queryset = FasciculosLista.objects.all().order_by('id')
		self.fields['fasciculo'].empty_label = "Selecione um fascículo"

class FotosAnuncioForms(forms.ModelForm):

	hide_condition = False

	checkBox_fotosAnuncios = forms.BooleanField( initial=False,
									required=False,
									label="Substituir todas as imagens",
									help_text='Em branco, manterá ou adicionará imagens')

	fotoAN = forms.FileField(   label="Selecione as fotos do anúncio",
								required=False,
								widget=forms.ClearableFileInput(attrs={
									'onclick' 	: "ImageADD(this);",
									'multiple'	: 'multiple',
									  'accept'	: 'image/*',
									  'class'	: 'inputFILE'})
							)

	class Meta:
		model = FotosAnuncio

		fields = ['fotoAN']

	def __init__(self, *args, **kwargs):

		hide_condition = kwargs.pop('hide_condition', False)
		super(FotosAnuncioForms, self).__init__(*args, **kwargs)

		print '*** hide_condition ***', hide_condition

		if not hide_condition:
			
			self.fields['checkBox_fotosAnuncios'].widget = forms.HiddenInput()
			#del self.fields['checkBox']

class NaveImagensForms(forms.ModelForm):

	piloto = forms.FileField(   label="Foto do Piloto",
								required=False,
								widget=forms.ClearableFileInput(attrs={
									'onclick' 	:"ImageChange(this);",
									'accept'	:'image/*',
									'class'		:'inputFILE'})
							)

	fotoCE = forms.FileField(   label="Escolha a cena do filme",
								required=False,
								widget=forms.ClearableFileInput(attrs={
									'onclick' 	:"ImageChange(this);",
									'accept'	:'image/*',
									'class'		:'inputFILE'})
							)
	fotoMo = forms.FileField(   label="Escolha a imagem do modelo",
								required=False,
								widget=forms.ClearableFileInput(attrs={
									'onclick' 	:"ImageChange(this);",
									'accept'	:'image/*',
									'class'		:'inputFILE'})
							)

	banner = forms.FileField(	label="Escolha a imagem para banner",
								required=False,
								widget=forms.ClearableFileInput(attrs={
									'onclick' 	:"ImageChange(this);",
									'accept'	:'image/*',
									'class'		:'inputFILE'})
							)

	class Meta:

		model = NaveImagens

		fields = ['piloto', 'fotoCE', 'fotoMo', 'banner']

class NaveForms(forms.ModelForm):

	class Meta:
		
		val = hashlib.sha512("Nave")
		arg = val.hexdigest()
		val = hashlib.sha512("naveNome")
		argb = val.hexdigest()

		model = Nave

		fields = ['naveNome', 'afiliacao', 'cores', 'poster', 'nomepiloto', 'fabricante']

		labels = {
			'naveNome'		: "Nome da Nave",
			'afiliacao'		: "Escolha a Afiliação.",
			'nomepiloto'	: "Digite o nome do Piloto",
			'poster'		: "Escolha o Poster"
		}

		widgets = {

			'naveNome'		: forms.TextInput(attrs={'placeholder'	: u'Digite o nome da Nave'
													,'size'			: '35'
													,'onclick' 		: "AutoComplete(this.id, '%s', '%s');" % (arg, argb)})     
        }
		help_text = {
			'afiliacao'		: "Escolha a afiliacao",
			'naveNome'		: "Digite o nome da nave"
		}

	def __init__(self, *args, **kwargs):
		super(NaveForms, self).__init__(*args, **kwargs)
		self.fields['afiliacao'].queryset = Afiliacao.objects.all().order_by('afiliacao')
		self.fields['afiliacao'].empty_label = "Selecione a afiliação"
		self.fields['cores'].queryset = Cores.objects.all().all().order_by('coresNom')
		self.fields['cores'].empty_label = "Selecione uma cor"
		self.fields['cores'].label = "Escolha uma cor"
		self.fields['poster'].queryset = Poster.objects.all().order_by('lancamento')
		self.fields['poster'].empty_label = "Selecione um Poster"
		self.fields['fabricante'].queryset = Fabricante.objects.all().order_by('fabricante')
		self.fields['fabricante'].empty_label = "Selecione um Fabricante"
		self.fields['fabricante'].label = "Escolha um Fabricante"

	def validNaveNome(self, objNave, editNave=None):
		naveValid = None
		try:
			naveValid = Nave.objects.get(naveNome=objNave['naveNome'].value())
			
			if editNave.id != naveValid.id:
				objNave.add_error('naveNome', "O nome para essa nave já existe")
		
		except Exception as e:
			print "NÃO exite registro *******************", e
			if Nave.objects.filter(naveNome=naveValid):
				objNave.add_error('naveNome', "O nome para essa nave já existe")

		return objNave
		
#DescricaoFormSet = inlineformset_factory(Caracteristica, Descricao, fields=('caracteristica', 'informacao'), form=DescricaoForms, can_delete = False)

class EstoqueForms(forms.ModelForm):

	class Meta:

		model = Estoque

		fields = ['estoqEntrada', 'valorUni']

	def clean_estoqAtual(self):
		print "estoqAtual ", self.cleaned_data.get('estoqAtual')
		print "estoqEntrada ", self.cleaned_data.get('estoqEntrada')
		print "valorUni ", self.cleaned_data.get('valorUni')


class VendaForms(forms.ModelForm):

	class Meta:

		model = Venda

		fields = ['quantidadeVenda', 'valorVenda']

		labels = {
			'quantidadeVenda'		: "Quantidade da venda",
			'valorVenda'			: "Valor da venda",

		}

	def clean_quantidadeVenda(self):

   		quantidadeVenda = self.cleaned_data.get('quantidadeVenda')

   		if int(quantidadeVenda) == 0:
			raise forms.ValidationError("A venda deve maior que [ %s ] itens." % quantidadeVenda)
		return quantidadeVenda

   		#raise forms.ValidationError("API Call failed")

class ProdutorForms(forms.ModelForm):


	class Meta:

		val = hashlib.sha512("Produtor")
		arg = val.hexdigest()
		val = hashlib.sha512("nomeProdutor")
		argb = val.hexdigest()

		print arg

		model = Produtor
		fields = ['nomeProdutor', 'fotoPR']

		label = {
				'nomeProdutor'	: "Nome do produtor"
		}

		widgets = {

			'nomeProdutor'		: forms.TextInput(attrs={'placeholder'	: u'Digite o nome do produtor'
														,'size'			: '35'
														,'onclick' 		: "AutoComplete(this.id, '%s', '%s');" % (arg, argb)})     
        }
		
	def clean_nomeProdutor(self):

		nomeProdutor = self.cleaned_data.get('nomeProdutor')

		if Produtor.objects.filter(nomeProdutor=nomeProdutor):
			raise forms.ValidationError(u'Essa produtor [ %s ] já existe' % nomeProdutor)
		return nomeProdutor



class ProdutoForms(forms.ModelForm):

	class Meta:

		model = Produto

		fields = ['produtoNome', 'produzido']

		exclude = ('produtoNome',)

	def __init__(self, *args, **kwargs):
		super(ProdutoForms, self).__init__(*args, **kwargs)
		self.fields['produzido'].queryset = Produtor.objects.all().order_by('nomeProdutor')
		self.fields['produzido'].empty_label = "Selecione o produtor"