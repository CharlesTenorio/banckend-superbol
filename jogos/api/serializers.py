from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from jogos.models import Jogo


class JogoSerializer(ModelSerializer):

    class Meta:
        model = Jogo
        fields = ['id_partida', 'id_time_casa', 'time_casa', 'id_time_visitante',
                   'time_visitante', 'id_liga', 'liga', 'cc', 'ss', 'data_partida',
                    'qtd_gol_casa', 'qtd_gol_visitante', 'realizada']

 