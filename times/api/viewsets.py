from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from times.models import Time, Risco
from .serializers import TimeSerializer, RiscoSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter


User = get_user_model()


class TimeViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome_time',)
   

class RiscoViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Risco.objects.all()
    serializer_class = RiscoSerializer
    
