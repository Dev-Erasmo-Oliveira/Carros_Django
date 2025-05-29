from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View

# view para o usuario pesquisar os carros que ja estão adicionados na loja


class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)

        return render(request, 'cars.html', {'cars': cars})


# view para adicionar o carro que o usuário quer e logo depois redirecionar para a lista de carros novamente

class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form})

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
