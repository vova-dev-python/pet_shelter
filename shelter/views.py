from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pet, Volunteer, ShelterLocation
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


def index(request):
    """View function for the home page of the site."""
    num_pets = Pet.objects.count()
    num_volunteers = Volunteer.objects.count()
    num_locations = ShelterLocation.objects.count()

    context = {
        "num_pets": num_pets,
        "num_volunteers": num_volunteers,
        "num_locations": num_locations,
    }

    return render(request, "shelter/index.html", context=context)


class PetListView(generic.ListView):
    model = Pet
    context_object_name = "pet_list"
    template_name = "shelter/pet_list.html"
    paginate_by = 5


class PetDetailView(generic.DetailView):
    model = Pet
    template_name = "shelter/pet_detail.html"
    context_object_name = "pet"


@login_required
@require_POST
def toggle_volunteer_assignment(request, pk):
    """View to assign/unassign the current volunteer to/from a specific pet."""
    pet = get_object_or_404(Pet, pk=pk)

    if request.user in pet.volunteers.all():
        pet.volunteers.remove(request.user)
    else:
        pet.volunteers.add(request.user)

    return redirect("shelter:pet-detail", pk=pk)


class PetCreateView(generic.CreateView):
    model = Pet
    fields = ["name", "age_months", "gender", "description", "animal_type", "location", "is_adopted"]
    template_name = "shelter/pet_form.html"
    success_url = reverse_lazy("shelter:pet-list")


class PetUpdateView(generic.UpdateView):
    model = Pet
    fields = ["name", "age_months", "gender", "description", "animal_type", "location", "is_adopted"]
    template_name = "shelter/pet_form.html"

    def get_success_url(self):
        return reverse_lazy("shelter:pet-detail", kwargs={"pk": self.object.pk})


class PetDeleteView(generic.DeleteView):
    model = Pet
    template_name = "shelter/pet_confirm_delete.html"
    success_url = reverse_lazy("shelter:pet-list")


User = get_user_model()


class VolunteerListView(generic.ListView):
    model = User
    template_name = "shelter/volunteer_list.html"
    context_object_name = "volunteer_list"
