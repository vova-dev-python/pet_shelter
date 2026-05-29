from django.contrib.auth.models import AbstractUser
from django.db import models


class AnimalType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ShelterLocation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Pet(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    name = models.CharField(max_length=100)
    age_months = models.IntegerField(help_text='Age in months')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    description = models.TextField()
    is_adopted = models.BooleanField(default=False)

    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE, related_name='pets')
    location = models.ForeignKey(
        ShelterLocation, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='pets'
    )

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.name} ({self.animal_type.name}, {self.age_months} m.o.)'
