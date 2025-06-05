from django.db.models.signals import pre_save, pre_delete, post_save, post_delete 
from django.dispatch import receiver
from cars.models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    
    ...


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    ...