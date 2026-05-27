from django.contrib.auth import get_user_model
from django.views.generic import ListView

User = get_user_model()


class VolunteerListView(ListView):
    model = User
    template_name = 'shelter/volunteer_list.html'
    context_object_name = 'volunteer_list'
