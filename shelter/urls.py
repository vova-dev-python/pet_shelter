from django.urls import path

from .views import (
    IndexView,
    PetListView,
    PetDetailView,
    PetCreateView,
    PetUpdateView,
    PetDeleteView,
    ToggleVolunteerAssignmentView,
)


app_name = 'shelter'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('pets/', PetListView.as_view(), name='pet-list'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
    path('pets/create/', PetCreateView.as_view(), name='pet-create'),
    path('pets/<int:pk>/update/', PetUpdateView.as_view(), name='pet-update'),
    path('pets/<int:pk>/delete/', PetDeleteView.as_view(), name='pet-delete'),
    path(
        'pets/<int:pk>/toggle-assignment/',
        ToggleVolunteerAssignmentView.as_view(),
        name='toggle-volunteer-assignment'
    ),
]
