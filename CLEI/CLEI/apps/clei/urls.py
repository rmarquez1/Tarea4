from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^presidente/cantArticulos$', 'CLEI.apps.clei.views.numero_articulos'),
    url(r'^presidente/aceptadosEmpatados$', 'CLEI.apps.clei.views.crear_aceptados_empatados'),
    url(r'^presidente/seleccionPais$', 'CLEI.apps.clei.views.seleccion_por_pais'),
)