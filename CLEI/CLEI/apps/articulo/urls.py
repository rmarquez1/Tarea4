from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^create/$', 'CLEI.apps.articulo.views.nuevo_articulo'),
    url(r'^topico/create/$', 'CLEI.apps.articulo.views.nuevo_topico'),
    url(r'^asignar/$', 'CLEI.apps.articulo.views.asignar_puntuacion'),
)