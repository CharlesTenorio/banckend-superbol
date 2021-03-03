from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from financeiros.models import PlanoContas, ContasReceber, ContasPagar




class PlanoSerializer(ModelSerializer):

    class Meta:
        model = PlanoContas
        fields = ['id_banca', 'plano_conta']

        read_only_fields = ['id']


class ContaReceberSerializer(ModelSerializer):
    
    class Meta:
        model = ContasReceber
        fields = ['id_banca', 'id_plano', 'descricao', 'id_apostas', 'codigo_doc', 
                 'data_movi', 'valor_recebido', 'valor_tota', 'status_rebe', 'comprovate']


class ContasPagarSerializer(ModelSerializer):
    
    class Meta:
        model = ContasPagar
        fields = ['id_plano', 'id_banca', 'descricao', 'codigo_doc', 
                   'data_mov', 'data_vencimento', 'data_pagamento', 'valor_total', 'valor_pago', 'status_pg', 'comprovate']

                