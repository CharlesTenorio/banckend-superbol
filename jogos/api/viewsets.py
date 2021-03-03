from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from jogos.models import Jogo
from .serializers import JogoSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class JogoViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
   