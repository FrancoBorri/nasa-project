from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=50)  # varchar(50)
    email = models.EmailField(unique=True)  # Evitar correos duplicados
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Fecha de cuando se crea el objeto
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Fecha cada vez que se guarda el objeto

    class Meta:  # Metadatos de la clase
        db_table = "User"
