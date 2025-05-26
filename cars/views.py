from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

# view para o usuario pesquisar os carros que ja estão adicionados na loja


def cars_view(request):
    cars = Car.objects.all()
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__contains=search)
    
    return render(
        request,
        'cars.html',
        {'cars': cars}
    )

# view para adicionar o carro que o usuário quer e logo depois redirecionar para a lista de carros novamente


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})
