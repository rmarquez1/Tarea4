#encoding:utf-8
from django.db import models

class Clei(models.Model):
    num_articulos = models.IntegerField(primary_key=True, verbose_name='Número de artículos')
