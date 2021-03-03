from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from apostas.models import Aposta
from apostas.models import DetalheAposta


class ApostaSerializer(ModelSerializer):

    class Meta:
        model = Aposta
        fields = ['id_aposta', 'id_cambista', 'id_cliente', 'nome', 'documento', 'tipo', 
                  'data_aposta', 'qtd_jogos', 'cotacao', 'total_apostado', 'possivel_retorno', 'ganhou']

        read_only_fields = ['id_aposta']


class DetalheApostaSerializer(ModelSerializer):
    
    class Meta:
        model = DetalheAposta
        fields = ['id_aposta', 'id_jogo', 'liga', 'time_casa', 'time_visitante', 'cotacao', 'status_cotacao']

