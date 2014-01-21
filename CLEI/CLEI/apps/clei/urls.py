from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^aceptables$', 'CLEI.apps.clei.views.mostrar_aceptables'),
)