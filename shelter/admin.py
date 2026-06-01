from django.contrib import admin

from .models import AnimalType, Pet, ShelterLocation

admin.site.register(AnimalType)
admin.site.register(Pet)
admin.site.register(ShelterLocation)
