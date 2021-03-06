from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'CLEI.apps.inicio.views.inicio'),
    url(r'/usuario/nuevo$', 'CLEI.apps.inicio.views.nuevo_usuario'),
    url(r'^ingresar/$', 'CLEI.apps.inicio.views.ingresar'),
    url(r'^registrar/$', 'CLEI.apps.inicio.views.registrar'),
    url(r'^privado/presidente$', 'CLEI.apps.inicio.views.privado_presidente'),
    url(r'^privado/miembro$', 'CLEI.apps.inicio.views.privado_miembro'),
    url(r'^cerrar/$', 'CLEI.apps.inicio.views.cerrar'),

)