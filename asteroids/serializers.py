from rest_framework import serializers
from .models import Asteroid, Tracked_asteroid


class AsteroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asteroid
        fields = "__all__"


class Tracked_asteroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracked_asteroid
        fields = "__all__"
