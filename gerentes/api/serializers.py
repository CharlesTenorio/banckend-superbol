from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from gerentes.models import Gerente


class GerenteSerializer(ModelSerializer):

    class Meta:
        model = Gerente
        fields = ['id_usuario', 'id_adm', 'nome', 'celular', 'ativo']

      