from django.db import models
from bancas.models import Banca
from apostas.models import Aposta
from django.conf import settings


class PlanoContas(models.Model):
    id_banca = models.ForeignKey(Banca, on_delete=models.PROTECT)
    plano_conta = models.CharField(max_length=40)



class ConasReceber(models.Model):
    id_banca = models.ForeignKey(Banca, on_delete=models.PROTECT)
    id_plano = models.ForeignKey(PlanoContas, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=40)
    id_apostas = models.ForeignKey(Aposta, on_delete=models.PROTECT, blank=True, null=True)
    codigo_doc = models.CharField(max_length=40)
    data_movi = models.DateTimeField(auto_created=True)
    valor_recebido = models.DecimalField(max_digits=9, decimal_places=2)
    valor_tota = models.DecimalField(max_digits=9, decimal_places=2)
    status_rebe = models.CharField(max_length=30, choices=settings.STATUS_CONTA)
    comprovate = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.descricao


class ConasPagar(models.Model):
    id_plano = models.ForeignKey(PlanoContas, on_delete=models.PROTECT)
    id_banca = models.ForeignKey(Banca, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=40)
    codigo_doc = models.CharField(max_length=40)
    data_mov = models.DateTimeField(auto_created=True)
    data_vencimento = models.DateField(null=True, blank=True)
    data_pagamento = models.DateField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=9, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=9, decimal_places=2)
    status_pg = models.CharField(max_length=30, choices=settings.STATUS_CONTA)
    comprovate = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.descricao
