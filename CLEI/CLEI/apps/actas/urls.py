from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^mostrarActas/$', 'CLEI.apps.actas.views.generar_acta'),
)