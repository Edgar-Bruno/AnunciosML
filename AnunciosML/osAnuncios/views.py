# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.forms.models import modelformset_factory  
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from django.forms.util import ErrorList

import json

from django.apps import apps

import hashlib

from django.shortcuts import get_object_or_404
from osAnuncios.forms import *
from osAnuncios.models import *
from django.db.models import Sum
from decimal import *
from django.core.files.uploadedfile import SimpleUploadedFile

from dal import autocomplete

"""class AfiliacaoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        qs = Afiliacao.objects.all()
        return qs"""

def autocompleteView(request):
	
	if request.is_ajax():

		modelA = None
		fieldA = None

		q = request.GET.get('term', '')

		try:

			app = apps.get_app_config('osAnuncios')
			for model in app.models:

				vAux = hashlib.sha512(model.title())

				if vAux.hexdigest() == request.GET['arg']:

					modelA = model.title()+"._meta.get_all_field_names()"
					
					for fieldM in eval(modelA):

						vAux = hashlib.sha512(fieldM)
						if vAux.hexdigest() == request.GET['argb']:

							fieldA = fieldM
							modelA = model.title()
							break
					break

			pesquisa = modelA+".objects.filter("+fieldA+"__contains = q)"

			auto = eval(pesquisa)

		except Exception as e:
				print "ERRO------ ",e
		#auto = Produtor.objects.filter(nomeProdutor__contains = q)[:20]

		results = []

		for i in auto:

			try:
				field = "i."+fieldA
			except Exception as e:
				print "ERRO------ ",e

			i_json = {}
			i_json['id'] = i.id

			i_json['value'] = eval(field)

			results.append(i_json)

		data = json.dumps(results)

	else:

		data = 'fail'

	mimetype = 'application/json'

	return HttpResponse(data, mimetype)

def homeView(request):

	context = {
			'titulo'	: "Bem vindo ao StarWars Naves e Veículos"
		}
	return render(request, 'StarWars/home.html',context)

def produtorView (request, title, action):

	context = {
			'form' 				: ProdutorForms(),
			'titulo'			: title,
			'action'			: action,
			'Valores_enumetados': enumerate(Produtor.objects.all()),
			'method'			: 'POST',
			'botao'				: 'Salvar',
			'Options'			: 'btn-primary'
		}

	if request.method == 'POST':

		objProdutor = ProdutorForms(request.POST or None, request.FILES)

		if objProdutor.is_valid():
			instance = objProdutor.save(commit=False)
			instance.save()

			del context['form']
			context['method'] = 'GET'
			context['botao'] = 'Voltar'
			context['Options'] = 'btn-info'
		else:

			#objProdutor._errors["nomeProdutor"] = ErrorList([u'EDGAR BRUNO AAHH'])
			context['form'] = objProdutor

	return render(request, 'default/produtor.html', context )

def afiliacaoView (request, title, action):

	context = {
			'form' 				: afiliacaoForms(),
			'titulo'			: title,
			'action'			: action,
			'Valores_enumetados': enumerate(Afiliacao.objects.all()),
			'method'			: 'POST',
			'botao'				: 'Salvar',
			'Options'			: 'btn-primary'
		}

	if request.method == 'POST':

		objAfi = AfiliacaoForms(request.POST or None, request.FILES)

		if objAfi.is_valid():
			instance = objAfi.save(commit=False)
			instance.save()

			del context['form']
			context['img'] = Afiliacao.objects.filter(id=instance.id)
			context['method'] = 'GET'
			context['botao'] = 'Voltar'
			context['Options'] = 'btn-info'
		else:

			context['form'] = objAfi

	return render(request, 'StarWars/formulario.html', context )

def posterView (request, title, action):

	context = {
			'form' 				: posterForms(),
			'titulo'			: title,
			'action'			: action,
			'Valores_enumetados': enumerate(Poster.objects.all()),
			'method'			: 'POST',
			'botao'				: 'Salvar',
			'Options'			: 'btn-primary'
		}

	if request.method == 'POST':

		objPoster = PosterForms(request.POST or None, request.FILES)

		if objPoster.is_valid():
			instance = objPoster.save(commit=False)
			instance.save()

			del context['form']
			context['img'] = Poster.objects.filter(id=instance.id)
			context['method'] = 'GET'
			context['botao'] = 'Voltar'
			context['Options'] = 'btn-info'
		else:

			context['form'] = objPoster

	return render(request, 'StarWars/formulario.html', context )

def caracteristicaView (request, title, action):

	context = {
			'form' 				: CaracteristicaForms(),
			'titulo'			: title,
			'action'			: action,
			'Valores_enumetados': enumerate(Caracteristica.objects.all()),
			'method'			: 'POST',
			'botao'				: 'Salvar',
			'Options'			: 'btn-primary'
		}

	if request.method == 'POST':

		objCaract = CaracteristicaForms(request.POST or None)

		if objCaract.is_valid():
			instance = objCaract.save(commit=False)
			instance.save()

			del context['form']
			context['method'] = 'GET'
			context['botao'] = 'Voltar'
			context['Options'] = 'btn-info'
		else:

			context['form'] = objCaract

	return render(request, 'StarWars/formulario.html', context )

def fabricanteView (request, title, action):

	context = {
			'form' 				: FabricanteForms(),
			'titulo'			: title,
			'action'			: action,
			'Valores_enumetados': enumerate(Fabricante.objects.all()),
			'method'			: 'POST',
			'botao'				: 'Salvar',
			'Options'			: 'btn-primary',
			'linkULR'			: 'fabricante'
		}

	if request.method == 'POST':

		objfabricante = FabricanteForms(request.POST or None, request.FILES)

		if objfabricante.is_valid():
			instance = objfabricante.save(commit=False)
			instance.save()

			del context['form']
			context['method'] = 'GET'
			context['botao'] = 'Voltar'
			context['Options'] = 'btn-info'
		else:

			context['form'] = objfabricante

	return render(request, 'StarWars/formulario.html', context )

def fabricanteEditarView (request, title):
	return render(request, 'StarWars/formulario.html', {})

def descricaoView (request, title, action):

	context = {
			'form' 				: DescricaoForms(),
			'titulo'			: title,
			'action'			: action,
			'Valores_enumetados': enumerate(Descricao.objects.all()),
			'LabelCarac'		: Caracteristica.objects.all(),
			'method'			: 'POST',
			'botao'				: 'Salvar',
			'Options'			: 'btn-primary'
		}

	if request.method == 'POST':

		objDesc = DescricaoForm(request.POST or None)

		if objDesc.is_valid():
			instance = objDesc.save(commit=False)
			instance.save()

			del context['form']
			context['method'] = 'GET'
			context['botao'] = 'Voltar'
			context['Options'] = 'btn-info'

		else:

			context['form'] = objDesc

	return render(request, 'StarWars/formulario.html', context )

def coresView(request, title, action):

	context = {
		'form' 				: coresForms,
		'titulo'			: title,
		'action'			: action,
		'method'			: 'POST',
		'botao'				: 'Salvar',
		'Options'			: 'btn-primary',
		'Valores_enumetados': enumerate(Cores.objects.all())
		}

	if request.method == 'POST':

		objCor = CoresForms(request.POST)

		print "cor ",objCor

		if objCor.is_valid():
			instance = objCor.save(commit=False)
			instance.save()

			del context['form']
			context['method'] = 'GET'
			context['botao'] = 'Voltar'
			context['Options'] = 'btn-info'
			
		else:

			context['form'] = objCor

	return render(request, 'StarWars/formulario.html', context )

def naveView (request, naveNome, title, addEdit):

	context = {
			'linkULR'			: "nave",
			'addEdit'			: addEdit,
			'AfiliacaoForm' 	: afiliacaoForms(),
			'PosterForm'		: posterForms(),
			'CoresForm'			: coresForms(),
			'FabricanteForm'	: fabricanteForms(),
			'method'			: 'POST',
			'botao'				: 'Salvar'
	}

	#Defini se ADD ou EDIT formulario nave
	editNave = None

	if addEdit:
		
		# "Edit True - Add False"
		editNave = get_object_or_404(Nave, naveNome=naveNome.replace('_',' ').replace('--', '\''))

		editItem = ItemCaracteristica.objects.get(nave_id=editNave.id)

		objNaveImagens = NaveImagens.objects.get(nave_id=editNave.id)

		objI = NaveImagens.objects.get(nave_id=editNave.id)

		objF = FotosAnuncio.objects.filter(nave_id=editNave.id)

		editProd = Produto.objects.get(id=editNave.id)

		InitialP = {	'id'				: editProd.id,
						'produzido'			: editProd.produzido.id,
					}

		InitialIMG = {	'id'				: objNaveImagens.id,
						'banner'			: objNaveImagens.banner,
						'piloto'			: objNaveImagens.piloto,
						'fotoMo'			: objNaveImagens.fotoMo,
						'fotoCE'			: objNaveImagens.fotoCE
					}

		InitialI = {'nave_id'			: editNave.id,
					'id'				: editItem.id,
					'dimecoes'			: editItem.dimecoes,
					'revista'			: editItem.revista,
				    'fasciculo'			: editItem.fasciculo.id,
					'extras'			: editItem.extras
				}
		
		DescricaoFormSet = modelformset_factory(Descricao, form=DescricaoForms)

		query = Descricao.objects.filter(nave_id=editNave.id)

		formsetForm = DescricaoFormSet(queryset = query)

		context.update({
			'objI'				: objI,
			'objF'				: FotosAnuncio.objects.filter(nave_id=editNave.id),
			'form' 				: NaveForms(instance=editNave),
			'formFosTa'			: NaveImagensForms(initial=InitialIMG),
			'formset'			: formsetForm,
			'formP'				: ProdutoForms(initial=InitialP),
			'formI'				: ItemCaracteristicaForms(initial=InitialI),
			'formF'				: FotosAnuncioForms(hide_condition=True)

		})
		
	else:
		# "Add True - Edit False"
		DescricaoFormSet = formsets.formset_factory(DescricaoForms)

		context.update({
			'form' 				: NaveForms(),
			'formFosTa'			: NaveImagensForms(),
			'formF'				: FotosAnuncioForms(),
			'formI'				: ItemCaracteristicaForms(),
			'formP'				: ProdutoForms(),
			'formset'			: DescricaoFormSet(),
			'Options'			: 'btn-primary',
			'titulo'			: title,
			
		})
	
	if request.method == 'POST':

		objNave = NaveForms(request.POST, instance=editNave or None)

		objNaveImagensPost = NaveImagensForms(request.POST or None, request.FILES)

		formProd = ProdutoForms(request.POST or None)

		formItem = ItemCaracteristicaForms(request.POST or None)

		obj_afiliacao = afiliacaoForms(request.POST or None, request.FILES)

		obj_poster = posterForms(request.POST or None, request.FILES)

		obj_cores = coresForms(request.POST or None)

		obj_fabricante = fabricanteForms(request.POST or None)
		
		formsetForm = DescricaoFormSet(request.POST or None)

		# Verifica todos os checkboX ADD
		updated_data = request.POST.copy()

		for fieldIN in objNave.fields:

			try:
				objField = eval("obj_" + fieldIN)

				#forms = eval(fieldIN + "Forms")
				checkbox = "checkBox_" + fieldIN

				if objField[checkbox].value():

					novoValor = objField

					valoresADD = novoValor.salveValueADD(objField)

					updated_data.update({fieldIN: int(valoresADD.id)})

					objNave = NaveForms(data=updated_data)

					#objField  = forms(data={checkbox: False})
					
					# checked = false
					objField.data[checkbox] = False
					
			except Exception as e:

				print "Error-----",e
				print fieldIN

		#--------------------------------------------------------

		# Verifica todos os checkboX ADD dos forms no FormSet
		# Recebe os valor em diversos formatos
		formsetADD_RAW = []
		
		for obj_item in formsetForm:
			
			obj_caracteristica = DescricaoForms()
		
			if obj_item['checkBox_descricao'].value():
				
				valorADD = obj_caracteristica.salveValueADD(obj_item)

				dic = {'caracteristica'		:  valorADD['addCaract'],
					   'informacao'			:  obj_item['informacao'].value(),
					   'caracteristicaADD'	:  obj_item['caracteristicaADD'].value()
					  }

				if valorADD['error']:
			
					dic.update({
								'checkBox_descricao'	:  True})		
				else:
					dic.update({
								'checkBox_descricao'	:  False})

				formsetADD_RAW.append(dic)
			else:

				formsetADD_RAW.append(obj_item)

		formsetADD_IN = []

		for formSetItem in formsetADD_RAW:
			dic = None
			try:
				formSetItem.fields
				print "formsetADD_RAW  >>> Captura do valores Formset"

				dic = {'caracteristica'		:  formSetItem['caracteristica'].value(),
					   'checkBox_descricao'	:  formSetItem['checkBox_descricao'].value(),
					   'informacao'			:  formSetItem['informacao'].value(),
					   'caracteristicaADD'	:  formSetItem['caracteristicaADD'].value()
					  }

				print "------------------------------------"
			except Exception as e:
				print "ERRO------ ",e
				print "formsetADD_RAW  >>> Captura do valores Lista"

				dic = {'caracteristica'		:  formSetItem['caracteristica'],
					   'checkBox_descricao'	:  formSetItem['checkBox_descricao'],
					   'informacao'			:  formSetItem['informacao'],
					   'caracteristicaADD'	:  formSetItem['caracteristicaADD']
					  }	
			
			formsetADD_IN.append(dic)

		for enu, item_ADD in enumerate(formsetADD_IN):

			caractFormsetUpdate = "form-%s-caracteristica" % enu
			checkBFormsetUpdate = "form-%s-checkBox_descricao" % enu

			updated_data[caractFormsetUpdate] = item_ADD['caracteristica']
			updated_data[checkBFormsetUpdate] = item_ADD['checkBox_descricao']
		
			updated_data.update({'caracteristica'		: item_ADD['caracteristica'],
								 'checkBox_descricao'	: item_ADD['checkBox_descricao'],
								 'informacao'			: item_ADD['informacao'],
								 'caracteristicaADD'	: item_ADD['caracteristicaADD']
								})

			"""print 'caracteristica      >', item_ADD['caracteristica']
												print 'checkBox_descricao  >', item_ADD['checkBox_descricao']
												print 'informacao          >', item_ADD['informacao']
												print 'caracteristicaADD   >', item_ADD['caracteristicaADD']
												print "*********************************************************"""

			formsetForm =  DescricaoFormSet(data=updated_data)

		#-------------------------------------------------------------------------
		# Valid naveName ADD / EDIT
		objName = NaveForms()
		objNave = objName.validNaveNome(objNave, editNave)

		if objNave.is_valid() and formProd.is_valid() and formItem.is_valid() and formsetForm.is_valid():

			if addEdit:
				# "Edit True - Add False"
				instance = objNave.save(commit=False)
				instance.save()

				instanceI = formItem.save(commit=False)

				# Verifica se o ID do ItemCaracteristica é EXISTENTE
				#	if InitialI.has_key('id'):
				instanceI.id = InitialI['id']
				instanceI.nave_id = editNave.id
				instanceI.save()


				for formSet in formsetForm.forms:
					formSetUpdate = formSet.save(commit=False)
					"""print formSetUpdate.id
				       print formSetUpdate.caracteristica_id
					   print formSetUpdate.nave_id
					   print "----------" """
					
					if formSetUpdate.caracteristica_id:
						formSetUpdate.nave_id = editNave.id
						formSetUpdate.save()

				if request.FILES.getlist("fotoAN"):
	                # on Substitui todas as imagens
					if request.POST.get('checkBox_fotosAnuncios'):
						FotosAnuncio.objects.filter(nave_id=editNave.id).delete()
					for key in request.FILES.getlist("fotoAN"):
						IMX = FotosAnuncio.objects.create(nave_id=instance.id, fotoAN=key)

				instanceNaIma = objNaveImagensPost.save(commit=False)

				instanceNaIma.id = InitialIMG['id']
				instanceNaIma.nave_id = instance.id

				for imgd in objNaveImagensPost.fields:
					imgdi = "instanceNaIma." + imgd
                    #print "-----  imgdi    %s -- %s  " % (imgdi, eval(imgdi))
                    #print "-----  fieldIMG %s -- %s  " % (fieldIMG, eval(fieldIMG))

					if not eval(imgdi):
						value = "%s = '%s'" % (imgdi, eval("objNaveImagens." + imgd))
						exec (value)
				
				instanceNaIma.save()

				url = reverse('exibir_nave', kwargs={ 'naveNome': instance.naveNome })

				return HttpResponseRedirect(url)

			else:
				# "Add True - Edit False"

				instance = objNave.save(commit=False)
				
				instanceP = formProd.save(commit=False)
				instanceP.produtoNome = instance.naveNome
				instanceP.save()

				instance.produto_id = instanceP.id
				instance.save()
				instanceI = formItem.save(commit=False)
				instanceI.nave_id = instance.id
				instanceI.save()	

				for formSet in formsetForm.forms:

					formUP = formSet.save(commit=False)
					if formUP.caracteristica_id:
						formUP.nave_id = instance.id
						formUP.save()

				instanceNaIma = objNaveImagens.save(commit=False)
				instanceNaIma.nave_id = instance.id
				instanceNaIma.save()

				for key in request.FILES.getlist("fotoAN"):
					IMX = FotosAnuncio.objects.create(nave_id=instance.id, fotoAN=key)

				del context['form']
				context['method'] = 'GET'
				context['botao'] = 'Voltar'
				context['Options'] = 'btn-info'
		
		else:

			print "objNave.is_valid()", objNave.is_valid()
			print "formProd.is_valid()", formProd.is_valid()
			print "formItem.is_valid()", formItem.errors
			print "formset.is_valid()", formsetForm.is_valid()

			context = {
				'addEdit'			: addEdit,
				'form' 				: objNave,
				'formFosTa'			: objNaveImagensPost,
				'formP'				: formProd,
				'formF'				: FotosAnuncioForms,
				'formset' 			: formsetForm,
				'formI'				: formItem,
				'AfiliacaoForm' 	: obj_afiliacao,
				'PosterForm'		: obj_poster,
				'CoresForm'			: obj_cores,
				'FabricanteForm'	: obj_fabricante,
				'method'			: 'POST',
		    	'botao'				: 'Salvar',
				'Options'			: 'btn-primary',
			}

	return render(request, 'StarWars/formADDnave.html', context )

def listagemView(request):

	# Uma forma de se criar um objeto
	objRAW = Nave.objects.raw("""SELECT
			 osAnuncios_nave.id,
			 osAnuncios_produto.id,
			 osAnuncios_naveimagens.banner,
			 osAnuncios_afiliacao.id,
			 osAnuncios_produto.produzido_id,
			 CONVERT(osAnuncios_afiliacao.afiliacao USING utf8),
			 osAnuncios_estoque.id,
			 osAnuncios_estoque.produto_id,
			 osAnuncios_estoque.atualizAtual,
			 osAnuncios_estoque.atualizEntrada,
			 osAnuncios_estoque.estoqAtual,
			 osAnuncios_estoque.estoqEntrada,
			 osAnuncios_estoque.valorUni,
			 osAnuncios_estoque.flat,
			 osAnuncios_venda.id,
			 osAnuncios_venda.produto_id,
			 osAnuncios_venda.estoque_id,
			 osAnuncios_venda.dataVenda,
		     SUM(CASE
				WHEN osAnuncios_venda.quantidadeVenda IS NOT NULL 
					THEN osAnuncios_venda.quantidadeVenda
			 END) AS vendasTotal,
			 CONVERT(SUM(osAnuncios_venda.valorVenda)USING utf8) AS valorVendasTotal
			 FROM osAnuncios_nave
			 INNER JOIN osAnuncios_naveimagens ON ( osAnuncios_naveimagens.nave_id = osAnuncios_nave.id )
			 INNER JOIN osAnuncios_produto ON ( osAnuncios_nave.produto_id = osAnuncios_produto.id )
			 INNER JOIN osAnuncios_afiliacao ON ( osAnuncios_nave.afiliacao_id = osAnuncios_afiliacao.id )
			 LEFT JOIN osAnuncios_estoque ON ( osAnuncios_estoque.produto_id = osAnuncios_produto.id )
			 LEFT JOIN osAnuncios_venda ON ( osAnuncios_venda.produto_id = osAnuncios_produto.id )
			 WHERE osAnuncios_estoque.flat = True OR osAnuncios_estoque.id IS NULL
			 GROUP BY osAnuncios_produto.id
			 ORDER BY osAnuncios_afiliacao.afiliacao, osAnuncios_nave.naveNome""")

	try:

		objSumEstoq = Estoque.objects.select_related().filter(produto__produzido_id=objRAW[0].produzido_id, flat=True).aggregate(Sum('estoqAtual')).values()[0]
		objSumVenda = Venda.objects.select_related().filter(produto__produzido_id=objRAW[0].produzido_id).aggregate(totalVenda=Sum('quantidadeVenda'), totalValor=Sum('valorVenda'))

		varPerc = Percentagem(objSumEstoq, objSumVenda)

		#print "Estoque %s | Vendas %s | PRODUZIDO %s" % (objSumEstoq, objSumVenda, objRAW[0].produzido_id)

	except Exception as e:

		print "Error-----",e
		objSumEstoq = 0
		objSumVenda = 0
		varPerc = 0	

	context ={
		'objRAW'	: objRAW,
		'linkULR'	: "nave",
		'objVEN'	: [objSumEstoq, objSumVenda, varPerc]
	}

	return render(request, 'StarWars/listagem.html', context )

def exibirNaveView (request, naveNome):

	checkNave = get_object_or_404(Nave, naveNome=naveNome.replace('_',' ').replace('--', '\''))

	#corObj = Cores.objects.get(id = checkNave.cores_id)
	posterObj = Poster.objects.get(id=checkNave.poster_id)
	
	descObj = Descricao.objects.select_related().filter(nave_id=checkNave.id)

	navePrev, naveNext = checkNave.get_next_preview_by_afiliacao()

	#x = ItemCaracteristica.objects.get(nave_id=checkNave.id)

	context = {
			'navePrev'			: navePrev,
			'naveNext'			: naveNext,
			'linkULR'			: "nave",
			'obj' 				: checkNave,
			'objNaFotos'		: NaveImagens.objects.get(nave_id=checkNave.id),
			'descricao'			: descObj,
			'Item'				: ItemCaracteristica.objects.get(nave_id=checkNave.id),
			'fotoanuncio'		: FotosAnuncio.objects.filter(nave_id=checkNave.id),
			'poster'			: posterObj,
			'cor'				: (".corprincipal{"
									"background-image: linear-gradient("
									"to right, black, %s, black); }")% str(checkNave.cores.coresHex)
			}

	return render(request, 'StarWars/anuncio.html', context )

def custom_404 (request):

	print "Aqui"
	print dir(request)
	print "-------"
	print request.user

	return render(request, 'custom_404.html', {'aqui': request} )

###########################################################################
def estoqueView (request, naveNome):

	naveNome = naveNome.replace('_',' ').replace('--', '\'')

	objNave = Nave.objects.get(naveNome = naveNome)

	estoque = {}

	if Estoque.objects.filter(produto_id=objNave.id):
		estoque = Estoque.objects.filter(produto_id=objNave.id).latest('atualizEntrada')

	context = {
			'estoque'			: estoque,
			'estoqueform' 		: EstoqueForms(),
			'method'			: 'POST',
			'botao'				: 'Salvar',
			'Options'			: 'btn-primary',
			'titulo'			: objNave
		}

	estoqueOBJ = EstoqueForms(request.POST or None)

	if estoqueOBJ.is_valid():

		instance = estoqueOBJ.save(commit=False)

		if Estoque.objects.filter(produto_id=objNave.id):
			objUlti = Estoque.objects.filter(produto_id=objNave.id).latest('atualizEntrada')
			objUlti.flat = False
			objUlti.save()
			instance.estoqAtual = objUlti.estoqAtual + instance.estoqEntrada

		else:
			instance.estoqAtual = instance.estoqEntrada

		instance.produto_id = objNave.id
		instance.save()

		del context['estoqueform']
		context['method'] = 'GET'
		context['botao'] = 'Voltar'
		context['action'] =  'nave'
		context['Options'] = 'btn-info'

		return HttpResponseRedirect(reverse('nave'))
		
	else:
		print"Não estoque"

	return render(request, 'StarWars/estoque.html', context )


def vendaView (request, naveNome):

	naveNome = naveNome.replace('_',' ').replace('--', '\'')

	objNave = Nave.objects.get(naveNome = naveNome)

	estoque = []

	if Estoque.objects.filter(produto_id=objNave.id):
		estoque = Estoque.objects.filter(produto_id=objNave.id).latest('atualizEntrada')

		context = {

			'method'			: 'POST',
			'botao'				: 'Vender',
			'Options'			: 'btn-primary',
			'vendasform' 		: VendaForms,
			'estoque'			: estoque,
			'titulo'			: naveNome
		}

		objVend = VendaForms(request.POST or None)

		# Verifica se há estoque suficiente para venda
		
		qtdV = int(objVend['quantidadeVenda'].value())
		#print "request.POST.getlist()[0]", request.POST.getlist('quantidadeVenda')[0]

		if qtdV > estoque.estoqAtual:
			
			objVend.add_error('quantidadeVenda', "Não há itens suficientes no estoque")
		
		else:

			print "Valor Menor", qtdV

		if objVend.is_valid():
			instanceV = objVend.save(commit=False)
			instanceV.produto_id = objNave.id
			instanceV.estoque_id = estoque.id

			estoque.estoqAtual = estoque.estoqAtual - qtdV
			estoque.save()

			instanceV.save()

		else:

			context['vendasform'] = objVend

	else:

		context = {

			'method'			: 'POST',
			'botao'				: 'Salvar',
			'Options'			: 'btn-primary',
			'titulo'			: "Não há estoque para venda"
		}

	return render(request, 'StarWars/venda.html', context )

#########

def formularioView(request):
	return None

def Percentagem(a, b):

	#varPerc = round(Decimal((objSumEstoq + objSumVenda['totalVenda']) - objSumEstoq)/Decimal(objSumEstoq + objSumVenda['totalVenda']),2) * 100
	perc = round(Decimal((a + b['totalVenda']) - a)/Decimal(a + b['totalVenda'])* 100, 2)
	return perc