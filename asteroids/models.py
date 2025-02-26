from django.db import models


class Asteroid(models.Model):
    name = models.CharField(max_length=50)
    estimated_diameter = models.FloatField()
    close_approach_date = models.DateField()  # Fecha de aproximación
    velocity = models.FloatField()
    distance_from_earth = models.FloatField()
    is_hazardous = models.BooleanField()

    class Meta:
        db_table = "asteroids"


class Tracked_asteroid(models.Model):  # Asteroides rastreados
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    asteroid = models.ForeignKey("asteroids.Asteroid", on_delete=models.CASCADE)
    traked_at = models.DateTimeField(
        auto_now_add=True
    )  # Fecha de rastreo, dia en que el usuario rastreo el asteroide

    class Meta:
        db_table = "tracked_asteroids"
