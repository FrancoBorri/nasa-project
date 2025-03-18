from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated 
import json
from users.models import User


# 🔹 Registro de usuario
def user_register(request):
    if request.method == 'POST':
        try:
            # Convierte el JSON a diccionario los datos de la request
            data = json.loads(request.body)

            # Validación del correo y nombre de usuario
            if User.objects.filter(username=data.get('username')).exists():
                return JsonResponse({'message': 'Username already exists'}, status=400)
            if User.objects.filter(email=data.get('email')).exists():
                return JsonResponse({'message': 'Email already exists'}, status=400)

            # Crear el usuario
            user = User.objects.create(
                username=data['username'],
                email=data['email'],
                password=data['password'],
            )
            user.set_password(data['password'])
            user.save()

            # Crear los tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            # Responder con un mensaje de éxito y los tokens
            return JsonResponse({
                'message': 'User created successfully',
                'access_token': access_token,
                'refresh_token': str(refresh)
            }, status=201)  # HTTP 201: Created
            
        except json.JSONDecodeError:
            # Error en caso de que el JSON esté mal formado
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            # Manejo general de errores
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request'}, status=405)




# 🔹 Crear usuario (POST)
def create_user(request):
    permission_classes = [IsAuthenticated]
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Convierte el JSON a diccionario los datos de la request

            # Validación del correo y nombre de usuario
            if User.objects.filter(username=data.get('username')).exists():
                return JsonResponse({'message': 'Username already exists'}, status=400)
            if User.objects.filter(email=data.get('email')).exists():
                return JsonResponse({'message': 'Email already exists'}, status=400)
            
            # Crear el usuario
            user = User.objects.create(
                username=data['username'],
                email=data['email'],
                password=data['password'],
            )

            # Encriptar la contraseña
            user.set_password(data['password'])
            user.save()
            return JsonResponse({'message': 'User created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    return JsonResponse({'message': 'Invalid request'}, status=405)


# 🔹 Listar usuarios (GET)
def list_users(request):
    permission_classes = [IsAuthenticated]
    if request.method == 'GET':
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    users = list(User.objects.values("id", "username", "email", "created_at","updated_at"))
    return JsonResponse(users, safe=False)


# 🔹 Obtener un usuario por ID (GET)
def get_user(request, user_id):
    permission_classes = [IsAuthenticated]
    user = get_object_or_404(User, id=user_id)
    return JsonResponse({"id": user.id, "username": user.username, "email": user.email, "created_at": user.created_at, "updated_at": user.updated_at})


# 🔹 Actualizar usuario (PUT)
def update_user(request, user_id):
    permission_classes = [IsAuthenticated]
    user = get_object_or_404(User, id=user_id) # Obtiene el usuario por ID
    if request.method == "PUT":
        data = json.loads(request.body) # Convierte el JSON a diccionario los datos de la request
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        if "password" in data:
            user.set_password(data["password"])  # Encripta si se cambia la contraseña
        user.save()
        return JsonResponse({"message": "Usuario actualizado"})


# 🔹 Eliminar usuario (DELETE)
def delete_user(request, user_id):
    permission_classes = [IsAuthenticated]
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return JsonResponse({"message": "Usuario eliminado"})


# 🔹 Pagina Bienvenida
def welcome(request):
    return JsonResponse({'message': 'Welcome to the users API'})