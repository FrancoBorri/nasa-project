from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from users.serializers import UserSerializer
from django.contrib.auth.models import User
