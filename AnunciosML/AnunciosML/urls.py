"""AnunciosML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.contrib import admin

from django.conf import settings
from django.contrib.staticfiles import views

from osAnuncios.models import Caracteristica

urlpatterns = [

    url(r'^autocomplete/', 'osAnuncios.views.autocompleteView'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^home/$', 'osAnuncios.views.homeView', name='home'),

    url(r'^nave/listagem/$', 'osAnuncios.views.listagemView', name='listagem'),

    url(r'^default/produtor$', 'osAnuncios.views.produtorView', {
            'title'     : 'Defina um Produtor',
            'action'    : 'produtor'}, name='produtor'),

    url(r'^formulario/afiliacao$', 'osAnuncios.views.afiliacaoView', {
            'title'     : 'Defina uma Afiliacao',
            'action'    : 'afiliacao'}, name='afiliacao'),
    url(r'^formulario/cor$', 'osAnuncios.views.coresView', {
            'title'     : 'Defina uma Cor',
            'action'    : 'cor'}, name='cor'),
    url(r'^formulario/poster$', 'osAnuncios.views.posterView', {
            'title'     : 'Defina um Poster',
            'action'    : 'poster'}, name='poster'),

    url(r'^formulario/caracteristica$', 'osAnuncios.views.caracteristicaView', {
            'title'     : 'Defina um Caracteristica',
            'action'    : 'caracteristica'}, name='caracteristica'),

    url(r'^formulario/fabricante$', 'osAnuncios.views.fabricanteView', {
            'title'     : 'Defina um Fabricante',
            'action'    : 'fabricante'}, name='fabricante'),

    #url(r'^formulario/descricao$', 'osAnuncios.views.descricaoView', {'title' : 'Defina um Caracteristica','action'    : 'descricao'}, name='descricao'),

    #Uniao ADD e EDITE
    url(r'^formulario/nave$', 'osAnuncios.views.naveView', {
            'naveNome'  : None,
            'title'     : 'Defina uma Nova Nave',
            'addEdit'   : False }, name='nave'),

    url(r'^formulario/editar/naves/(?P<naveNome>[-\w]+)/$', 'osAnuncios.views.naveView', {
            'title'     : 'Defina uma Editar_nave',
            'addEdit'   : True }, name='editar_nave'),


    url(r'^exibir/naves/(?P<naveNome>[-\w]+)/$', 'osAnuncios.views.exibirNaveView', name='exibir_nave'),
    
    #url(r'^formulario/editar/naves/(?P<naveNome>[-\w]+)/$', 'osAnuncios.views.editarNaveView', {
    #        'title'     : 'Edite os dados da nave'}, name='Editar_nave'),

    #url(r'^imperial/(?P<nome>[-\w]+)/$', 'osAnuncios.views.imperial'),

    url(r'^nave/estoque/(?P<naveNome>[-\w]+)/$', 'osAnuncios.views.estoqueView', name='estoque_nave'),

    url(r'^nave/venda/(?P<naveNome>[-\w]+)/$', 'osAnuncios.views.vendaView', name='venda_nave'),



]


"""handler404 = 'osAnuncios.views.custom_404'

print handler404"""

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)