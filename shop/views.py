from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm


def pets_list(request):
	context = {
		"pets": Pet.objects.all()
	}
	return render(request, 'pets_list.html', context)


def pet_details(request, pet_id):
	context = {
		"pet" : Pet.objects.get(id=pet_id)
	}
	return render(request, "pet_details.html", context)


def delete_pet(request, pet_id):
	Pet.objects.get(id=pet_id).delete()
	return redirect("pets-list")


def create_pet(request):
	form = PetForm()

	if request.method == 'POST':
		form = PetForm(request.POST)
		if form.is_valid():
			pet = form.save()
			return redirect("pet-details", pet.id)

	context = {
		"form" : form
	}
	return render(request, 'create_pet.html', context)


def update_pet(request, pet_id):
	pet = Pet.objects.get(id=pet_id)
	form = PetForm(instance=pet)

	if request.method == 'POST':
		form = PetForm(request.POST, instance=pet)
		if form.is_valid():
			pet = form.save()
			return redirect("pet-details", pet.id)

	context = {
		"form" : form,
		"pet":pet
	}
	return render(request, 'update_pet.html', context)
