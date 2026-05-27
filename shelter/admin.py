from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Volunteer, AnimalType, Pet, ShelterLocation


class VolunteerAdmin(UserAdmin):
    model = Volunteer
    list_display = ['username', 'email', 'phone_number', 'experience_years', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('phone_number', 'experience_years', 'pets')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {'fields': ('phone_number', 'experience_years', 'pets')}),
    )


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(AnimalType)
admin.site.register(Pet)
admin.site.register(ShelterLocation)
