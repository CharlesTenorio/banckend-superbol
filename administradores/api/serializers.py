from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from administradores.models import Administrador
#from clientes.models import CartaoCredito


class AdministradorSerializer(ModelSerializer):

    class Meta:
        model = Administrador
        fields = ['id_usuario', 'id_banca', 'nome', 'celular', 'ativo']

        read_only_fields = ['id_usuario', 'id']
