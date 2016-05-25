from django.conf.urls import url, inclue, patterns
from .views import autocompleteView

print "*******************" "URLS out"

urlpatterns = [

    url(r'^autocompleteView/', 'osAnuncios.views.autocompleteView', name='autocompleteView'),

    url(r'^autocompleteView/', autocompleteView)

]