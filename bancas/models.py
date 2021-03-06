from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()
class Banca(models.Model):
    id_usuario = models.OneToOneField(
        User, on_delete=models.PROTECT)

    nome_banca = models.CharField(max_length=80, unique=True)
    resposavel_banca = models.CharField(max_length=80)
    cpf_resposavel = models.CharField(max_length=20, unique=True)
    celular = models.CharField(max_length=15, unique=True)
    fone = models.CharField(max_length=15)
    cep = models.CharField("CEP *", max_length=10)
    logradouro = models.CharField("Logradouro *", max_length=80)
    numero = models.CharField("Número *", max_length=5)
    complemento = models.CharField(max_length=30, null=True, blank=True)
    bairro = models.CharField("Bairro *", max_length=40)
    localidade = models.CharField("Cidade *", max_length=50)
    uf = models.CharField("Estado *", max_length=2,
                          default='PE', choices=settings.ESTADOS_CHOICES)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.nome_banca

    class Meta:
        db_table = 'banca'
        managed = True
        verbose_name = 'Banca'
        verbose_name_plural = 'Bancas'

