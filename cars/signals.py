from django.db.models.signals import post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    # query para calcular a quantidade de carros e o valor total do estoque
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
# criação na tabela CarsInventory com os valores tanto dos carros quanto do estoque e armazenar na tabela
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )
