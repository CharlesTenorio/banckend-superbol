from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()



class Cliente(models.Model):
    id_usr = models.OneToOneField(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=40)
    foto = models.ImageField(verbose_name='Foto', null=True,  blank=True)
    nascimento = models.DateField()
    cpf = models.CharField(max_length=20, unique=True)
    numero_pix = models.CharField(max_length=150, unique=True)
    data_cad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'cliente'
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Conta(models.Model):
    id_apostador = models.OneToOneField(Cliente, on_delete=models.PROTECT)
    saldo_total = models.DecimalField(max_digits=9, decimal_places=2)
    bonus_total = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self):
            return self.id_apostador

    class Meta:
        db_table = 'conta'
        managed = True
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

class HistorioConta(models.Model):
    id_conta = models.ForeignKey(Conta, on_delete=models.PROTECT)
    movimentacao= models.CharField(max_length=20, choices=settings.TIPO_MOVIMENTACAO)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    movi_data = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return self.movimentacao

    class Meta:
        db_table = 'historicoconta'
        managed = True
        verbose_name = 'historico'
        verbose_name_plural = 'historicos'
