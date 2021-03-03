from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from bancas.models import Banca


class BancaSerializer(ModelSerializer):

    class Meta:
        model = Banca
        fields = ['id_usuario', 'nome_banca', 'resposavel_banca', 'cpf_resposavel',
                  'celular', 'fone', 'cep', 'logradouro', 'numero', 'complemento', 
                  'bairro', 'localidade', 'uf', 'data_cadastro', 'ativo']

        read_only_fields = ['id_usuario', 'id']
