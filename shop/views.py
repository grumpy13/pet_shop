from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm

def pet_list(request):
    context = {
        "pets": Pet.objects.all()
    }
    return render(request, 'pet_list.html', context)

def pet_detail(request, pet_id):
    context = {
        "pet": Pet.objects.get(id=pet_id)
    }
    return render(request, 'pet_detail.html', context)

def pet_create(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet_obj= form.save()
            return redirect('pet-details', pet_obj.id)
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def pet_update(request, pet_id):
    pet_obj = Pet.objects.get(id=pet_id)
    form = PetForm(instance=pet_obj)
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES, instance=pet_obj)
        if form.is_valid():
            form.save()
            return redirect('pet-details', pet_obj.id)
    context = {
        "pet_obj": pet_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def pet_delete(request, pet_id):
    pet_obj = Pet.objects.get(id=pet_id)
    pet_obj.delete()
    return redirect('pets-list')