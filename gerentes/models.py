from django.db import models
from django.contrib.auth import get_user_model

from administradores.models import Administrador

User = get_user_model()

class Gerente(models.Model):
    id_usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    id_adm = models.ForeignKey(Administrador, on_delete=models.PROTECT) 
    nome = models.CharField(max_length=40)
    celular = models.CharField(max_length=20, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


# Create your models here.
