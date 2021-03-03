from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from cambistas.models import Cambista

from .serializers import CambistaSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


from rest_framework.permissions import IsAuthenticated


class CambistaViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Cambista.objects.all()
    serializer_class = CambistaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome',)
