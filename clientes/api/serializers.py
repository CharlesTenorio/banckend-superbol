from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from clientes.models import Cliente, Conta, HistorioConta




class ClienteSerializer(ModelSerializer):

    class Meta:
        model = Cliente
        fields = ['id_usr', 'nome', 'foto', 'nascimento', 'cpf', 'numero_pix', 'data_cad']

        read_only_fields = ['id_usr', 'id']


class ContaSerializer(ModelSerializer):
    
    class Meta:
        model = Conta
        fields = ['id_apostador', 'saldo_total', 'bonus_total']


class HistoricoContaSerializer(ModelSerializer):
    
    class Meta:
        model = HistorioConta
        fields = ['id_conta', 'movimentacao', 'valor', 'movi_data']

                