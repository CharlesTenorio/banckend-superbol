from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from gerentes.models import Gerente
from .serializers import GerenteSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated


User = get_user_model()




class GerenteViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Gerente.objects.all()
    serializer_class = GerenteSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome',)
