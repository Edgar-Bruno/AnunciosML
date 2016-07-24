
from django.conf.urls import include, url, patterns

urlpatterns = patterns('osAnuncios.views',

	url(r'^autocomplete/', 'autocompleteView'),


    url(r'^home/$', 'homeView', name='home'),

    url(r'^nave/listagem/$', 'listagemView', name='listagem'),

    url(r'^default/produtor$', 'produtorView', {
            'title'     : 'Defina um Produtor',
            'action'    : 'produtor'}, name='produtor'),

    url(r'^formulario/afiliacao$', 'afiliacaoView', {
            'title'     : 'Defina uma Afiliacao',
            'action'    : 'afiliacao'}, name='afiliacao'),
    url(r'^formulario/cor$', 'coresView', {
            'title'     : 'Defina uma Cor',
            'action'    : 'cor'}, name='cor'),
    url(r'^formulario/poster$', 'posterView', {
            'title'     : 'Defina um Poster',
            'action'    : 'poster'}, name='poster'),

    url(r'^formulario/caracteristica$', 'caracteristicaView', {
            'title'     : 'Defina um Caracteristica',
            'action'    : 'caracteristica'}, name='caracteristica'),

    url(r'^formulario/fabricante$', 'fabricanteView', {
            'title'     : 'Defina um Fabricante',
            'action'    : 'fabricante'}, name='fabricante'),

    #url(r'^formulario/descricao$', 'descricaoView', {'title' : 'Defina um Caracteristica','action'    : 'descricao'}, name='descricao'),

    #Uniao ADD e EDITE
    url(r'^formulario/nave$', 'naveView', {
            'naveNome'  : None,
            'title'     : 'Defina uma Nova Nave',
            'addEdit'   : False }, name='nave'),

    url(r'^formulario/editar/naves/(?P<naveNome>[-\w]+)/$', 'naveView', {
            'title'     : 'Defina uma Editar_nave',
            'addEdit'   : True }, name='editar_nave'),


    url(r'^exibir/naves/(?P<naveNome>[-\w]+)/$', 'exibirNaveView', name='exibir_nave'),
    
    #url(r'^formulario/editar/naves/(?P<naveNome>[-\w]+)/$', 'editarNaveView', {
    #        'title'     : 'Edite os dados da nave'}, name='Editar_nave'),

    #url(r'^imperial/(?P<nome>[-\w]+)/$', 'imperial'),

    url(r'^nave/estoque/(?P<naveNome>[-\w]+)/$', 'estoqueView', name='estoque_nave'),

    url(r'^nave/venda/(?P<naveNome>[-\w]+)/$', 'vendaView', name='venda_nave'),

)
