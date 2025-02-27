from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer



class User_create(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.validate_email(request.data['email']):
            serializer.save() # Guarda el objeto en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
