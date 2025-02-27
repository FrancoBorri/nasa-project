from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_username(self, username):
        if User.objects.filter(user_name=username).exists():
            raise serializers.ValidationError("Username already exists")
        return username

    def validate_email(self, email):
        # realizar consultas en la base de datos filter(), get(), create(), update(), etc.
        if User.objects.filter(email=email).exists():
            # raise lanzador de errores en python
            raise serializers.ValidationError("Email already exists")
        return email

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError(
                "La contraseña debe contener al menos 8 caracteres"
            )
        if not any(char.isalpha() for char in password):
            raise serializers.ValidationError(
                "La contraseña debe contener al menos una letra"
            )
        return password
