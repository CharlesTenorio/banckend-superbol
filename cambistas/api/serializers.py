from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from cambistas.models import Cambista


class CambistaSerializer(ModelSerializer):

    class Meta:
        model = Cambista
        fields = ['id_usuario', 'id_gerente', 'nome', 'cpf', 'sexo', 'nascimento', 'celular', 
                   'cep', 'logradouro', 'numero', 'complemento', 
                    'bairro', 'localidade', 'uf', 'data_cad', 'ativo']

        read_only_fields = ['id_usuario', 'id']
