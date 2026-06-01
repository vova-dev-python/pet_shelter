from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Pet, ShelterLocation


class IndexView(TemplateView):
    """View class for the home page of the site."""
    template_name = 'shelter/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_pets'] = Pet.objects.count()
        user = get_user_model()
        context['num_volunteers'] = user.objects.count()
        context['num_locations'] = ShelterLocation.objects.count()
        return context


class PetListView(ListView):
    model = Pet
    context_object_name = 'pet_list'
    template_name = 'shelter/pet_list.html'
    paginate_by = 5


class PetDetailView(DetailView):
    model = Pet
    template_name = 'shelter/pet_detail.html'
    context_object_name = 'pet'


class ToggleVolunteerAssignmentView(LoginRequiredMixin, View):
    """View to assign/unassign the current volunteer to/from a specific pet."""

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        pet = get_object_or_404(Pet, pk=pk)

        if request.user in pet.volunteers.all():
            pet.volunteers.remove(request.user)
        else:
            pet.volunteers.add(request.user)

        return redirect('shelter:pet-detail', pk=pk)


class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    fields = ['name', 'age_months', 'gender', 'description', 'animal_type', 'location', 'is_adopted']
    template_name = 'shelter/pet_form.html'
    success_url = reverse_lazy('shelter:pet-list')


class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = ['name', 'age_months', 'gender', 'description', 'animal_type', 'location', 'is_adopted']
    template_name = 'shelter/pet_form.html'

    def get_success_url(self):
        return reverse_lazy('shelter:pet-detail', kwargs={'pk': self.object.pk})


class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'shelter/pet_confirm_delete.html'
    success_url = reverse_lazy('shelter:pet-list')
