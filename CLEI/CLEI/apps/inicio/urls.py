from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'$', 'CLEI.apps.inicio.views.inicio'),
)