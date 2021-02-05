from django.db import models
from django.contrib.auth import get_user_model
from gerentes.models import Gerente
from django.conf import settings

User = get_user_model()

class Cambista(models.Model):
    id_usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    id_gerente = models.ForeignKey(Gerente, on_delete=models.PROTECT)
    nome = models.CharField(max_length=80)
    cpf= models.CharField(max_length=20, unique=True)
    sexo = models.CharField(max_length=15)
    nascimento = models.DateField()
    celular = models.CharField(max_length=20, default='0')
    cep = models.CharField("CEP *", max_length=10)
    logradouro = models.CharField("Logradouro *", max_length=80)
    numero = models.CharField("Número *", max_length=5)
    complemento = models.CharField(max_length=30, null=True, blank=True)
    bairro = models.CharField("Bairro *", max_length=40)
    localidade = models.CharField("Cidade *", max_length=50)
    uf = models.CharField("Estado *", max_length=2,
                          default='PE', choices=settings.ESTADOS_CHOICES)
    data_cad = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Cambista'
        verbose_name_plural = 'Cambistas'

    def __str__(self):
        return self.nome

