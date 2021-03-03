from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from financeiros.models import PlanoContas, ContasReceber, ContasPagar
from .serializers import ContaReceberSerializer, ContasPagarSerializer, PlanoSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


class PlanoViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = PlanoContas.objects.all()
    serializer_class = PlanoSerializer
   

class ContaPgViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = ContasPagar.objects.all()
    serializer_class = ContasPagarSerializer
    
class ContaRecebeViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = ContasReceber.objects.all()
    serializer_class = ContaReceberSerializer
    