from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from usuarios.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name']
        read_only_fields = ['id_usuario']
        extra_kwargs={'password':{'write_only': True}}

    def save(self):
        user = User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name']
        )
        password=self.validated_data['password'],


        user.set_password(password)
        user.save()
        return user
