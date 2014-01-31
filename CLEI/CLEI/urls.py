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
    url(r'^evento/', include('CLEI.apps.evento.urls')),
    url(r'^actas/', include('CLEI.apps.actas.urls')),
    url(r'^eventos/', include('CLEI.apps.eventos.urls')),
)
urlpatterns += patterns('',
               (r'^imagenes/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
)
