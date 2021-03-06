from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^presidente/cantArticulos$', 'CLEI.apps.clei.views.cantidad_articulos'),
    url(r'^presidente/aceptadosEmpatados$', 'CLEI.apps.clei.views.crear_aceptados_empatados'),
    url(r'^presidente/seleccionDesempate$', 'CLEI.apps.clei.views.seleccion_desempate'),
    url(r'^presidente/seleccionPais$', 'CLEI.apps.clei.views.seleccion_por_pais'),
    url(r'^presidente/estadosSeleccion$', 'CLEI.apps.clei.views.mostrar_estados_finales'),
    url(r'^presidente/seleccionProporcionPais$', 'CLEI.apps.clei.views.seleccion_por_pais_proporcion'),
    url(r'^presidente/seleccionProporcionTopico$', 'CLEI.apps.clei.views.seleccion_por_topico_proporcion'),
)
