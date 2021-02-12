from django.db import models
from times.models import Time
from ligas.models import Liga

class Jogo(models.Model):
    id_partida = models.BigIntegerField(unique=True)
    id_time_casa = models.ForeignKey(Time, on_delete=models.PROTECT, related_name='casa')
    time_casa = models.CharField(max_length=80)
    id_time_visitante = models.ForeignKey(Time, on_delete=models.PROTECT, related_name='visitante')
    time_visitante = models.CharField(max_length=80)
    id_liga = models.ForeignKey(Liga, on_delete=models.PROTECT)
    liga = models.CharField(max_length=80)
    cc = models.CharField(max_length=2)
    ss =  models.CharField(max_length=4)
    data_partida = models.DateTimeField()
    qtd_gol_casa = models.PositiveIntegerField(default=0)
    qtd_gol_visitante = models.PositiveIntegerField(default=0)
    realizada = models.BooleanField()
    
    
    
    def __str__(self):
        self.liga

    class Meta:
        db_table = 'jogo'
        managed = True
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
