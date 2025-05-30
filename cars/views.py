from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView

# view para o usuario pesquisar os carros que ja estão adicionados na loja

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


# view para adicionar o carro que o usuário quer e logo depois redirecionar para a lista de carros novamente

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'