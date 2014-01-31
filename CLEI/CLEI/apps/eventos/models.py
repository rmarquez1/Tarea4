from django.db import models

class Evento(models.Model):
    nombre      = models.CharField(max_length=200)
    tipo        = models.CharField(max_length=30)
    fecha       = models.DateField('fecha del evento')
    inicio      = models.TimeField('hora de inicio')
    duracion    = models.IntegerField('Duracion (min)')

    def __unicode__(self):
        return self.nombre
