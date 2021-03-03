from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from apostas.models import Aposta, DetalheAposta
from .serializers import ApostaSerializer, DetalheApostaSerializer
from rest_framework.permissions import IsAuthenticated


class ApostaViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Aposta.objects.all()
    serializer_class = ApostaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('documento',)
    

class DetalheApostaViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = DetalheAposta.objects.all()
    serializer_class = DetalheApostaSerializer
