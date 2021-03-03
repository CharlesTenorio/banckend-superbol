from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from times.models import Time, Risco



class TimeSerializer(ModelSerializer):

    class Meta:
        model = Time
        fields = ['id_time', 'nome_time', 'cc', 'image_id', 'data_cad']

        read_only_fields = ['data_cad']


class RiscoSerializer(ModelSerializer):
    
    class Meta:
        model = Risco
        fields = ['id_time', 'descricao_risco', 'valor_risco']

