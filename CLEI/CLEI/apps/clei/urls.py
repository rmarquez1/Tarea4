from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^cantArticulos$', 'CLEI.apps.clei.views.numero_articulos'),
    url(r'^aceptadosEmpatados$', 'CLEI.apps.clei.views.crear_aceptados_empatados'),
)