from django.contrib.auth.models import AbstractUser
from django.db import  models
    
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # Muestra mas claro el email en el panel de admin
        return self.email
    
    class Meta:
        db_table = "user" # Nombre de la tabla en la base de datos