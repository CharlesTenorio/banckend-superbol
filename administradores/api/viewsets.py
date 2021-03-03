from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from administradores.models import Administrador

from .serializers import AdministradorSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


from rest_framework.permissions import IsAuthenticated


class AdministradorViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome',)
