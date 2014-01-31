from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CLEI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('CLEI.apps.inicio.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articulo/', include('CLEI.apps.articulo.urls')),
    url(r'^participante/', include('CLEI.apps.participante.urls')),
    url(r'^privado/clei/', include('CLEI.apps.clei.urls')),
    url(r'^eventos/$', 'eventos.views.generar_programa'),
    url(r'^eventos/(?P<evento_id>\d+)/$', 'eventos.views.mostrar'),
)
urlpatterns += patterns('',
               (r'^imagenes/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
)
