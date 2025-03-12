from rest_framework import serializers
from .models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:  # Define configuraciones para el serializador
        model = User
        fields = "__all__"

    def validate_username(self, user_name):
        if User.objects.filter(user_name).exists():
            raise serializers.ValidationError("El usuario ya esta registrado")
        else:
            return user_name

    def validate_email(self, email):
        if User.objects.filter(email).exists():
            raise serializers.ValidationError("El email ya esta registrado")
        return email
