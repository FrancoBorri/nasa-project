from rest_framework import status
from rest_framework.exeptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer


class UserCreate(APIView):  # Crear usuario
    def post(self, request):
        serializer = UserSerializer(
            data=request.data
        )  # Creo instancia del serializador
        if serializer.is_valid():  # Valido con el metodo is_valid()
            serializer.save()  # Guardo en BD
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):  # Obtener un usuario
    def get(self, pk):
        try:
            # Busco el usuario en la base de datos.
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        # Serializamos el usuario y lo devolvemos en la respuesta
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserList(APIView):  # Listar usuarios
    # Especifica los permisos y la autenticacion
    permission_clases = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserUpdate(APIView):  # Actualizar usuario
    def put(self, request, pk):
        try:
            # Buscar el usuario por su ID
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            # Si no se encuentra el usuario, retornamos un error 404
            raise NotFound(detail="Usuario no encontrado")

        # Serializamos los datos de la request para validarlos
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            # Si los datos son válidos, guardamos los cambios
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Si los datos no son válidos, retornamos un error 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, pk):
        try:
            # Obtener el usuario a eliminar
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            # Si no existe el usuario, se lanza una excepción 404
            raise NotFound("Usuario no encontrado")
        # Eliminar el usuario
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
