from django.contrib.auth.models import AbstractUser
from django.db import models


class Volunteer(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    pets = models.ManyToManyField('shelter.Pet', related_name='volunteers', blank=True)

    def __str__(self) -> str:
        return f'{self.username} ({self.experience_years} yrs exp)'
