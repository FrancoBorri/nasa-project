from rest_framework import serializers
from .models import Astronomical_images, Favourite_images


class Astronomical_imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Astronomical_images
        fields = "__all__"


class Favourite_imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite_images
        fields = "__all__"
