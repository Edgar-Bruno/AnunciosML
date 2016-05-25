# -*- coding: utf-8 -*-
from django import template
from decimal import *

register = template.Library()

@register.filter
def margemLucro(value, args):

	""" LEGENDA
		value = estoque.valorUni
		args.split()[0] = venda.quantidadeVenda => vendasTotal
		args.split()[1] = venda.valorVenda => valorVendasTotal
		round(Decimal((a + b['totalVenda']) - a)/Decimal(a + b['totalVenda']),2 ) * 100

	"""
	args = "{:.2f}".format((Decimal(args.split()[1]) - (Decimal(args.split()[0]) * value))/Decimal(args.split()[1])*100)

	return args

@register.filter
def proximoAfi(value, args):
	
	if value[int(args)].afiliacao == value[int(args)-1].afiliacao:
		# "MANDEM DIV", value[int(args)].afiliacao
		return False
	elif args > 0:
			#"FECHA DIV %s 
		return 2
	else:
		# CRIA NOVA DIV %s" % (value[int(args)-1].afiliacao, value[int(args)].afiliacao)
		return True

@register.filter
def espacoReplace(value):

	return str(value).replace(' ','_')

@register.filter
def tooltipM(value, args):

	obj = []

	for index, val in enumerate(value):
		
		try:
			if value[int(args) + index].afiliacao == value[int(args)].afiliacao:
				#print "SIM  %s , agr %s" %  (value[int(index) + arg ].afiliacao, arg)
				obj.append(value[int(args) + index])

			else:
				break

		except Exception as e:

			print "Error-----",e
			break

	return obj

@register.filter
def fieldCAT(value, args):
	
	for field in value:
		if field.name == args:
			return field


