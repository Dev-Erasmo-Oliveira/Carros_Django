from django import forms
from cars.models import Car


# Classe que irá adicionar todos os campos preenchidos no nosso banco de dados
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


    #função para validar se o carro vale mais de R$ 120 mil
    def clean_value(self):
       value = self.cleaned_data.get('value')
       if value < 120000:
           self.add_error('value', 'O valor mínimo do carro deve ser de R$ 120.000')
       else:
          return value
          
    #função para validar o ano de fabricação do carro
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2017:
            self.add_error('factory_year' , 'Não aceitamos carros fabricados antes do ano de 2017')
        return factory_year