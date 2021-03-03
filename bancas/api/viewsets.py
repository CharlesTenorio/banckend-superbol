from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from bancas.models import Banca

from .serializers import BancaSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


from rest_framework.permissions import IsAuthenticated


class BancaViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Banca.objects.all()
    serializer_class = BancaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome_banca',)
