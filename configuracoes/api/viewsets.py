from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from configuracoes.models import Configuracao
from rest_framework.permissions import IsAuthenticated
from .serializers import ConfiguracaoSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class ConfigViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Configuracao.objects.all()
    serializer_class = ConfiguracaoSerializer
    
