from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import AnimalType, Pet, ShelterLocation


class ShelterTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='TestVolunteer',
            password='password123'
        )

        self.dog_type = AnimalType.objects.create(name='Dog')
        self.shelter_location = ShelterLocation.objects.create(name='Lviv')

        self.pet = Pet.objects.create(
            name='Rex',
            animal_type=self.dog_type,
            location=self.shelter_location,
            age_months=20,
            description='Active dog.'
        )

    def test_pet_model_str(self) -> None:
        self.assertEqual(str(self.pet), 'Rex (Dog, 20 m.o.)')

    def test_pet_creation_fields(self) -> None:
        self.assertEqual(self.pet.animal_type.name, 'Dog')
        self.assertEqual(self.pet.location.name, 'Lviv')
        self.assertEqual(self.pet.age_months, 20)

    def test_homepage_status_code(self) -> None:
        response = self.client.get(reverse('shelter:index'))
        self.assertEqual(response.status_code, 200)

    def test_pet_list_page_status_code(self) -> None:
        response = self.client.get(reverse('shelter:pet-list'))
        self.assertEqual(response.status_code, 200)

    def test_volunteer_list_page_status_code(self) -> None:
        response = self.client.get(reverse('shelter:volunteer-list'))
        self.assertEqual(response.status_code, 200)

    def test_anonymous_user_cannot_toggle_volunteer(self) -> None:
        url = reverse('shelter:toggle-pet-assignment', kwargs={'pk': self.pet.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_can_join_care_team(self) -> None:
        self.client.login(username='TestVolunteer', password='password123')
        url = reverse('shelter:toggle-pet-assignment', kwargs={'pk': self.pet.pk})

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.pet.volunteers.filter(id=self.user.id).exists())

    def test_authenticated_user_can_leave_care_team(self) -> None:
        self.pet.volunteers.add(self.user)
        self.client.login(username='TestVolunteer', password='password123')
        url = reverse('shelter:toggle-pet-assignment', kwargs={'pk': self.pet.pk})

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.pet.volunteers.filter(id=self.user.id).exists())
