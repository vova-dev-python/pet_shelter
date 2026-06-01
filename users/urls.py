from django.urls import path

from .views import VolunteerListView

app_name = 'users'

urlpatterns = [
    path('volunteers/', VolunteerListView.as_view(), name='volunteer-list'),
]
