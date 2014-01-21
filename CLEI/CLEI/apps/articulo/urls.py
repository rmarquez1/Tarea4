from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^create/$', 'CLEI.apps.articulo.views.nuevo_articulo'),
    url(r'^topico/create/$', 'CLEI.apps.articulo.views.nuevo_topico'),
    url(r'^asignar/presidente$', 'CLEI.apps.articulo.views.asignar_puntuacion_presidente'),
    url(r'^asignar/miembro$', 'CLEI.apps.articulo.views.asignar_puntuacion_miembro'),
    #url(r'^aceptables$', 'CLEI.apps.articulo.views.crear_aceptables'),
)