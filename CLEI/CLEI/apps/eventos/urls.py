from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'CLEI.apps.eventos.views.generar_programa'),
    url(r'^(?P<evento_tipo_evento>.*)/$', 'CLEI.apps.eventos.views.mostrar'),
)