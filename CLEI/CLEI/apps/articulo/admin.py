from django.contrib import admin
from .models import Articulo, Topico, Puntuacion

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Topico)
admin.site.register(Puntuacion)