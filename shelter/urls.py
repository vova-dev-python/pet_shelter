from django.urls import path

from .views import (
    index,
    PetListView,
    PetDetailView,
    toggle_volunteer_assignment,
    PetCreateView,
    PetUpdateView,
    PetDeleteView,
    VolunteerListView
)

urlpatterns = [
    path("", index, name="index"),
    path("pets/", PetListView.as_view(), name="pet-list"),
    path("pets/<int:pk>/", PetDetailView.as_view(), name="pet-detail"),
    path("pets/<int:pk>/toggle-assign/", toggle_volunteer_assignment, name="toggle-pet-assignment"),

    path("pets/create/", PetCreateView.as_view(), name="pet-create"),
    path("pets/<int:pk>/update/", PetUpdateView.as_view(), name="pet-update"),
    path("pets/<int:pk>/delete/", PetDeleteView.as_view(), name="pet-delete"),
    path("volunteers/", VolunteerListView.as_view(), name="volunteer-list"),
]

app_name = "shelter"
