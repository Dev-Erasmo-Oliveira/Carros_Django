# Generated by Django 5.2.1 on 2025-05-14 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brand_alter_car_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='nome',
            new_name='name',
        ),
    ]
