from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from clientes.models import Cliente, Conta, HistorioConta
from .serializers import ClienteSerializer, ContaSerializer, HistoricoContaSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


from rest_framework.permissions import IsAuthenticated


class ClienteViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome',)


class ContaViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    
class HistoricoContaViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = HistorioConta.objects.all()
    serializer_class = HistoricoContaSerializer
    