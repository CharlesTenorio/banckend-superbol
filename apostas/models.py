from django.db import models
from cambistas.models import Cambista
from bancas.models import Banca
from clientes.models import Cliente
from jogos.models import Jogo
from django.conf import settings
import uuid


class Aposta(models.Model):
    id_aposta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_cambista = models.ForeignKey(Cambista, blank=True, null=True, on_delete=models.SET_NULL)
    id_cliente= models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    nome = models.CharField(max_length=40)
    documento = models.CharField(max_length=20, default='cpf')
    tipo = models.CharField(max_length=60, choices=settings.TIPO_APOSTA) 
    data_aposta = models.DateTimeField(auto_now=True)
    qtd_jogos = models.PositiveIntegerField(default=1)
    cotacao = models.DecimalField(max_digits=9, decimal_places=2)
    total_apostado = models.DecimalField(max_digits=9, decimal_places=2)
    possivel_retorno = models.DecimalField(max_digits=9, decimal_places=2)
    ganhou = models.BooleanField(default=False)

    def __str__(self):
            return self.nome

    class Meta:
        db_table = 'aposta'
        managed = True
        verbose_name = 'Aposta'
        verbose_name_plural = 'Apostas'

    
# Create your models here.
class DetalheAposta(models.Model):
        id_aposta=models.ForeignKey(Aposta, on_delete=models.PROTECT, related_name='det_aposta')
        id_jogo = models.ForeignKey(Jogo, on_delete=models.PROTECT)
        liga = models.CharField(max_length=40)
        time_casa = models.CharField(max_length=40)
        time_visitante=models.CharField(max_length=40)
        status = models.CharField(max_length=40, default='Aberta')
        cotacao = models.DecimalField(max_digits=9, decimal_places=2, default=0)
        status_cotacao = models.CharField(max_length=40, choices=settings.STATUS_COTACAO)

        
