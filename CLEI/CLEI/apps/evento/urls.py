from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     
    url(r'^social/$',       'CLEI.apps.evento.views.evento_social'),
    url(r'^simultaneo/$',   'CLEI.apps.evento.views.evento_simultaneo'),
    url(r'^lugar/$',        'CLEI.apps.evento.views.nuevo_lugar'),
    url(r'^lugar/asignar/$','CLEI.apps.evento.views.asignar_lugar'),
    url(r'^lugar/asignar_simultaneo/$','CLEI.apps.evento.views.asignar_lugar_simultaneo'),
    url(r'^lista/$',        'CLEI.apps.evento.views.lista_evento'),
    url(r'^lista_asignados/$','CLEI.apps.evento.views.lista_asignados'),
    url(r'^calendario/$',   'CLEI.apps.evento.views.crear_fecha')
)
