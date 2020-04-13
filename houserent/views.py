from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import City, Houses
from .forms import CityForm, HouseForm


@login_required
def city_list(request):
    cities = City.objects.all()
    return render(request, 'houserent/city_list.html', {'cities': cities})
@login_required
def city_detail(request, pk):
    citi = City.objects.get(id=pk)
    return render(request, 'houserent/city_detail.html', {'citi': citi})
@login_required
def city_create(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save()
            return redirect('city_detail', pk=city.pk)
    else:
        form = CityForm()
    return render(request, 'houserent/city_form.html', {'form': form})
@login_required
def city_edit(request, pk):
    city = City.objects.get(pk=pk)
    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            city = form.save()
            return redirect('city_detail', pk=city.pk)
    else:
        form = CityForm(instance=city)
    return render(request, 'houserent/city_form.html', {'form': form})
@login_required
def city_delete(request, pk):
    City.objects.get(id=pk).delete()
    return redirect('city_list') 
@login_required
def house_list(request):
    housess = Houses.objects.all()
    return render(request, 'houserent/house_list.html', {'housess': housess})
@login_required
def house_detail(request, pk):
    house = Houses.objects.get(id=pk)
    return render(request, 'houserent/house_detail.html', {'house': house})
@login_required
def house_create(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            houses = form.save()
            return redirect('house_detail', pk=houses.pk)
    else:
        form = HouseForm()
    return render(request, 'houserent/house_form.html', {'form': form})
@login_required
def house_edit(request, pk):
    house = Houses.objects.get(pk=pk)
    if request.method == "POST":
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            fad = form.save()
            return redirect('house_detail', pk=house.pk)
    else:
        form = HouseForm(instance=house)
    return render(request, 'houserent/house_form.html', {'form': form})
@login_required
def house_delete(request, pk):
    Houses.objects.get(id=pk).delete()
    return redirect('house_list') 