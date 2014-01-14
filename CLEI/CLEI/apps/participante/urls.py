from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^miembro/create/$', 'CLEI.apps.participante.views.nuevo_miembro'),
    url(r'^autor/create/$', 'CLEI.apps.participante.views.nuevo_autor'),
)