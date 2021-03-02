from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from consultores.models import Consultor
from clientes.models import Cliente

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        User = get_user_model()

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name': user.get_full_name()
        })

class CustomAuthTokenConsultor(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        cli = Consultor.objects.filter(id_usuario=user.pk).first()
        if cli:
            return Response({
               'token': token.key,
               'user_id': user.pk,
               'email': user.email,
               'name': user.get_full_name(),
               'id_consutor': cli.id
              })
        else:
            return Response({"msg":'consultor nao encontrado'}, status=404)



class CustomAuthTokenCliente(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        cli = Cliente.objects.filter(id_usuario=user.pk).first()
        if cli:
            return Response({
               'token': token.key,
               'user_id': user.pk,
               'email': user.email,
               'name': user.get_full_name(),
               'id_cliente': cli.id
              })
        else:
            return Response({"msg":'cliente nao encontrado'}, status=404)





@api_view(['POST',])
def registra_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "usuario cadastardo com sucesso"
        else:
            data = serializer.errors

        return Response(data)
