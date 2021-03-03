from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from ligas.models import Liga


class LigaSerializer(ModelSerializer):

    class Meta:
        model = Liga
        fields = ['id', 'nome', 'cc', 'has_leaguetable', 'has_toplist']

        