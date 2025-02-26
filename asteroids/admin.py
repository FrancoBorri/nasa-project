from django.contrib import admin
from .models import Asteroid, Tracked_asteroid

# Register your models here.

admin.site.register(Asteroid)
admin.site.register(Tracked_asteroid)
